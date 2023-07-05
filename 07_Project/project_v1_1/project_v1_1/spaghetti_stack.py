from aws_cdk import CfnOutput, Stack
from aws_cdk import aws_autoscaling as autoscaling
import aws_cdk.aws_ec2 as ec2
from constructs import Construct
from aws_cdk import aws_elasticloadbalancingv2 as elbv2
from project_v1_1.config import user_data


class Spaghetti_Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

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
        
    # MGMT VPC:
        # self.mgmtvpc = ec2.Vpc(self, "MGMTVPC",
        #                     # 1 AZ, 1 subnet
        #                    max_azs=1,
        #                    ip_addresses=ec2.IpAddresses.cidr("10.20.20.0/24"),
        #                    subnet_configuration=[ec2.SubnetConfiguration(
        #                        subnet_type=ec2.SubnetType.PUBLIC,
        #                        name="Public"
        #                     ),
        #                    ],
        #                    # nat_gateway_provider=ec2.NatProvider.gateway(),
        #                    nat_gateways=0,
        # )

    # VPC Peering:
        # Peering_connection = ec2.CfnVPCPeeringConnection(self, "Cloud10VPCPeer",
        #     peer_vpc_id=self.mgmtvpc.vpc_id,
        #     vpc_id=self.webvpc.vpc_id,

    
        # )

    ####################
    # Security Groups: #
    ####################

    # Management Server:
#         mgmt_sg=ec2.SecurityGroup(self, "MGMTSG",
#                                     vpc=self.mgmtvpc,
#                                     allow_all_outbound=False,)
       
#         mgmt_sg.add_ingress_rule(
#             ec2.Peer.any_ipv4(), ec2.Port.tcp(3389)) # RDP Access from ALL. Add trusted IP later
# # Allow RDP on Management Server:
#         mgmt_sg.connections.allow_from_any_ipv4(
#             ec2.Port.tcp(3389), "Allow RDP on Management Server from ALL") # Add trusted IP later


    #Webserver:
        WS_SG = ec2.SecurityGroup(self, "WebServerSG",
                                 vpc=webvpc,
                                 allow_all_outbound=False
        )
        
           
 #       WS_SG.connections.allow_from(
 #           mgmt_sg, ec2.Port.tcp(22), " Allow SSH from Management Server") 
       
    # Load Balancer:
        ws_lb_sg = ec2.SecurityGroup(self, "WebServerLoadBalancerSG",
                                 vpc=webvpc,
                                 allow_all_outbound=False
                                 )
        
   
    #############
    # Instances #
    #############
    

    # Create the Management Server instance
    #     mgmtserver_instance = ec2.Instance(
    #         self,
    #         "MGMTServer",
    #         instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO),
    #         machine_image=ec2.MachineImage.latest_windows(ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE),
    #         security_group=mgmt_sg,
    #         block_devices=[
    #             ec2.BlockDevice(
    #                 device_name="/dev/xvda",
    #                 volume=ec2.BlockDeviceVolume.ebs(
    #                     volume_size=8,
    #                     encrypted=True,
    #                     delete_on_termination=True,
    #                 )
    #             )],

    #         key_name="WebServerKey", # Imports the key pair. Make sure you create the key pair first!
    #         vpc=self.mgmtvpc,
    #         vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),  # Use public subnet
            
    #     )
    # # Output local IP of Management Server:
    #     CfnOutput(self, "MGMTServer IP:", value=mgmtserver_instance.instance_public_ip)

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
                                                    security_group=ws_lb_sg,
                                                    )
    # Output the Public IP (DNS Name) of the load balancer:
        CfnOutput(self, "WebServer_Public_IP", value=webserver_lb.load_balancer_dns_name)
    
    #Create Target Group for Webserver:
        webserver_tg = elbv2.ApplicationTargetGroup(self, "WebServerTargetGroup",
                                                    vpc=webvpc,
                                                    port=80,
                                                    protocol=elbv2.ApplicationProtocol.HTTP,
                                                    target_type=elbv2.TargetType.INSTANCE
                                                    )
        webserver_tg.add_target(webserver_instance)
    # Link ELB to Web Server:
        

        listener = webserver_lb.add_listener("Listener", default_target_groups=[webserver_tg], protocol=elbv2.ApplicationProtocol.HTTP)

  
        listener.connections.allow_from_any_ipv4(
            ec2.Port.tcp(443), "Allow HTTPS from All")
        
        listener.connections.allow_to_any_ipv4(
            ec2.Port.tcp(80), "Allow HTTP to All")

        listener.connections.allow_to_any_ipv4(
            ec2.Port.tcp(443), "Allow HTTPS to All")
        
 
    # # Redirect HTTP to HTTPS: -> To make it work, change protocol of listener to HTTPS, and add certificate.
    #     webserver_lb.add_redirect(
    #                     source_protocol=elbv2.ApplicationProtocol.HTTP,
    #                     source_port=80,
    #                     target_protocol=elbv2.ApplicationProtocol.HTTPS,
    #                     target_port=443,
    #                     )   