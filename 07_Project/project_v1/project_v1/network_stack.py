from aws_cdk import CfnOutput, Stack
from aws_cdk import aws_autoscaling as autoscaling
import aws_cdk.aws_ec2 as ec2
from constructs import Construct
from aws_cdk import aws_elasticloadbalancingv2 as elbv2
from project_v1.config import user_data
            
class Network_Stack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        ################################
        # Setting up the Webserver VPC #
        ################################

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
                           # nat_gateway_provider=ec2.NatProvider.gateway(),
                           nat_gateways=0,
                           )
        self.webvpc = webvpc

        # Create autoscaling group for Web Server:
        webserver_instance = autoscaling.AutoScalingGroup(
            self,
            "Webserver",
            vpc=webvpc,
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO
            ),
            machine_image=ec2.MachineImage.latest_amazon_linux2(),
            key_name="WebServerKey", # Imports the key pair. Make sure you create the key pair first!
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),  # Use public subnet
            user_data=ec2.UserData.custom(user_data),

            min_capacity=1,
            max_capacity=4,
        )
        

        # Build Load Balancer for Webserver:
        webserver_lb = elbv2.ApplicationLoadBalancer(self, "WebServerLB",
                                                    vpc=webvpc,
                                                    internet_facing=True,
                                                    load_balancer_name="WebServerLB",
                                                    )
        # Output the Public IP (DNS Name) of the load balancer:
        CfnOutput(self, "WebServer_Public_IP", value=webserver_lb.load_balancer_dns_name)
        
        # Link ELB to Web Server:
        listener = webserver_lb.add_listener("Listener", port=80)
        listener.add_targets("Target", port=80, targets=[webserver_instance])
        #Allow port 80 and 443 for everyone:
        listener.connections.allow_from_any_ipv4(ec2.Port.tcp(443), "Allow HTTPS")
        listener.connections.allow_from_any_ipv4(ec2.Port.tcp(80), "Allow HTTP")

        webserver_instance.scale_on_request_count("AModestLoad", target_requests_per_minute=60)
        


        #Setting up the MGMT VPC:
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
                
        #Build VPC Peering:
        cfn_vPCPeering_connection = ec2.CfnVPCPeeringConnection(self, "Cloud10VPCPeer",
            peer_vpc_id=self.mgmtvpc.vpc_id,
            vpc_id=self.webvpc.vpc_id,

    
        )
        # Create the Management Server instance
        mgmtserver_instance = ec2.Instance(
            self,
            "MGMTServer",
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO),
            machine_image=ec2.MachineImage.latest_windows(ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE),
            key_name="WebServerKey", # Imports the key pair. Make sure you create the key pair first!
            vpc=self.mgmtvpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),  # Use public subnet
            
        )
     
        # Output local IP of Management Server:
        CfnOutput(self, "MGMTServer IP:", value=mgmtserver_instance.instance_private_ip)


       
        #Security Groups:

        #On webserver, allow ports 80 & 443 to be publicly accessable:
        webserver_instance.connections.allow_from_any_ipv4(
            ec2.Port.tcp(80), "Allow http from internet")
        webserver_instance.connections.allow_from_any_ipv4(
            ec2.Port.tcp(443), "Allow https from internet")

        # On the default security group of the web server, give the Management Server exclusive access to the Web Server via SSH, block from other IPs.
        webserver_instance.connections.allow_from(mgmtserver_instance, ec2.Port.tcp(22), "Allow SSH from Management Server") 

        # Allow RDP on Management Server:
        mgmtserver_instance.connections.allow_from_any_ipv4(
            ec2.Port.tcp(3389), "Allow RDP from Management Server")

        
                