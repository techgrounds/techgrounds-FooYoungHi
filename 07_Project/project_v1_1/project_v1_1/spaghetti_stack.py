from aws_cdk import CfnOutput, Stack
from aws_cdk import aws_autoscaling as autoscaling
import aws_cdk.aws_ec2 as ec2
from constructs import Construct
from aws_cdk import aws_elasticloadbalancingv2 as elbv2
from project_v1_1.config import user_data
            
class Spaghetti_Stack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

    #################################
    # Setting up the VPCs & Peering #
    #################################

    # WebVPC:
        webvpc = ec2.Vpc(self, "WebServerVPC",
                            # 1 AZ, 2 subnets. 1 Public en 1 Isolated
                           max_azs=2,
                           ip_addresses=ec2.IpAddresses.cidr("10.10.10.0/24"),
                           subnet_configuration=[ec2.SubnetConfiguration(
                               subnet_type=ec2.SubnetType.PUBLIC,
                               name="Public"
                            ),
                            ec2.SubnetConfiguration(
                                subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                                name="Database"        
                            ),
                           ],
                           )
        self.webvpc = webvpc

        self.mgmtvpc = ec2.Vpc(self, "MGMTVPC",
                            # 1 AZ, 1 subnet
                           max_azs=1,
                           ip_addresses=ec2.IpAddresses.cidr("10.20.20.0/24"),
                           subnet_configuration=[ec2.SubnetConfiguration(
                               subnet_type=ec2.SubnetType.PUBLIC,
                               name="Public"
                            ),
                           ],
                           # nat_gateway_provider=ec2.NatProvider.gateway(),
                           nat_gateways=0,
        )

    # VPC Peering:
        Peering_connection = ec2.CfnVPCPeeringConnection(self, "Cloud10VPCPeer",
            peer_vpc_id=self.mgmtvpc.vpc_id,
            vpc_id=self.webvpc.vpc_id,

    
        )

    ####################
    # Security Groups: #
    ####################

    # Management Server:
        mgmt_sg=ec2.SecurityGroup(self, "MGMTSG",
                                    vpc=self.mgmtvpc,
                                    allow_all_outbound=False,)
       
        mgmt_sg.add_ingress_rule(
            ec2.Peer.any_ipv4(), ec2.Port.tcp(3389)) # RDP Access from ALL. Add trusted IP later


    #Webserver:
        WS_SG = ec2.SecurityGroup(self, "WebServerSG",
                                 vpc=webvpc,
                                 allow_all_outbound=False
        )
        
        WS_SG.add_ingress_rule(ec2.Peer.any_ipv4(), 
        ec2.Port.tcp(80),
        description="Allow HTTP from ALL"
        ) 

        WS_SG.add_ingress_rule(ec2.Peer.any_ipv4(), ec2.Port.tcp(443)), # Allow https from HTTPS
        
        WS_SG.connections.allow_from(
            mgmt_sg, ec2.Port.tcp(22), " Allow SSH from Management Server") 
       
    # Allow RDP on Management Server:
        mgmt_sg.connections.allow_from_any_ipv4(
            ec2.Port.tcp(3389), "Allow RDP on Management Server from ALL") # Add trusted IP later

    # Load Balancer:
        ws_lb_sg = ec2.SecurityGroup(self, "WebServerLoadBalancerSG",
                                 vpc=webvpc,
                                 allow_all_outbound=False
                                 )
        
    # Allow Incoming traffic from HTTP:
        ws_lb_sg.add_ingress_rule(ec2.Peer.any_ipv4(),
         ec2.Port.tcp(80), "Allow HTTP from ALL")
    # Allow incoming traffic from HTTPS:
        ws_lb_sg.add_ingress_rule(ec2.Peer.any_ipv4(),
         ec2.Port.tcp(443), "Allow HTTPS from ALL")

    # Allow outgoing traffic from HTTP to webserver:
        ws_lb_sg.connections.allow_to(WS_SG,
         ec2.Port.tcp(80), "Allow HTTP to WebServer")
    # Allow outgoing traffic from HTTPS to webserver:
        ws_lb_sg.connections.allow_to(WS_SG,
         ec2.Port.tcp(443), "Allow HTTPS to WebServer")


    #############
    # Instances #
    #############
    

    # Create the Management Server instance
        mgmtserver_instance = ec2.Instance(
            self,
            "MGMTServer",
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO),
            machine_image=ec2.MachineImage.latest_windows(ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE),
            security_group=mgmt_sg,
            block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/xvda",
                    volume=ec2.BlockDeviceVolume.ebs(
                        volume_size=8,
                        encrypted=True,
                        delete_on_termination=True,
                    )
                )],

            key_name="WebServerKey", # Imports the key pair. Make sure you create the key pair first!
            vpc=self.mgmtvpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),  # Use public subnet
            
        )
    # Output local IP of Management Server:
        CfnOutput(self, "MGMTServer IP:", value=mgmtserver_instance.instance_public_ip)

    # Create autoscaling group for Web Server:
        webserver_instance = autoscaling.AutoScalingGroup(
            self,
            "Webserver",
            vpc=webvpc,
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO
            ),
            machine_image=ec2.MachineImage.latest_amazon_linux2(),
            security_group=WS_SG,
            key_name="WebServerKey", # Imports the key pair. Make sure you create the key pair first!
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),  # Use public subnet
            block_devices=[
                autoscaling.BlockDevice(
                    device_name='/dev/xvda',
                    volume=autoscaling.BlockDeviceVolume.ebs(
                        volume_size=8,
                        encrypted=True,
                    )
                )],

            user_data=ec2.UserData.custom(user_data),

            min_capacity=1,
            max_capacity=3,
        )
        
    ################################
    # Load Balancer for Webserver: #
    ################################

    # Build Load Balancer for Webserver:
        webserver_lb = elbv2.ApplicationLoadBalancer(self, "WebServerLB",
                                                    vpc=webvpc,
                                                    internet_facing=True,
                                                    load_balancer_name="WebServerLB",
                                                    security_group=ws_lb_sg,                                                    )
    # Output the Public IP (DNS Name) of the load balancer:
        CfnOutput(self, "WebServer_Public_IP", value=webserver_lb.load_balancer_dns_name)
        
    # Link ELB to Web Server:
        listener = webserver_lb.add_listener("Listener", port=80)
        listener.add_targets("Target", port=80, targets=[webserver_instance])
    #Allow port 80 and 443 for everyone:
        listener.connections.allow_from_any_ipv4(ec2.Port.tcp(443), "Allow HTTPS")
        listener.connections.allow_from_any_ipv4(ec2.Port.tcp(80), "Allow HTTP")

        webserver_instance.scale_on_request_count("AModestLoad", target_requests_per_minute=60)
