from aws_cdk import CfnOutput, Stack
import aws_cdk.aws_ec2 as ec2
from constructs import Construct
            
class Spaghetti_Stack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Setting up the first VPC

        self.vpc = ec2.Vpc(self, "WebServerVPC",
                            # 1 AZ, 2 subnets. 1 Public en 1 Isolated
                           max_azs=1,
                           ip_addresses=ec2.IpAddresses.cidr("10.10.10.0/24"),
                           subnet_configuration=[ec2.SubnetConfiguration(
                               subnet_type=ec2.SubnetType.PUBLIC,
                               name="Public",
                               cidr_mask=24
                           )
                           ],
                           # nat_gateway_provider=ec2.NatProvider.gateway(),
                           nat_gateways=0,
                           )


        # Create an EC2 instance
        webserver_instance = ec2.Instance(
            self,
            "WebServer",
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO),
            machine_image=ec2.MachineImage.latest_amazon_linux2(),
            key_name="WebServerKey", # Imports the key pair. Make sure you create the key pair first!
            vpc=self.vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),  # Use public subnet
            user_data=ec2.UserData.custom("""#!/bin/bash
                                    # Install Apache Web Server and PHP
                                    yum install -y httpd php
                                    # Turn on web server
                                    chkconfig httpd on
                                    service httpd start""")
        )
        # Security Group for Webserver: Allow http from all sources, and SSH from all sources.
        webserver_instance.connections.allow_from_any_ipv4(
            ec2.Port.tcp(22), "Allow ssh from internet")
        webserver_instance.connections.allow_from_any_ipv4(
            ec2.Port.tcp(80), "Allow http from internet")
        webserver_instance.connections.allow_from_any_ipv4(
            ec2.Port.tcp(443), "Allow https from internet")

        CfnOutput(self, "Output", value=self.vpc.vpc_id)