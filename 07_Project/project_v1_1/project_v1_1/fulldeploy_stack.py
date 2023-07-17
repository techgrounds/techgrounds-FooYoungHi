from aws_cdk import (CfnOutput, Stack, Duration,
aws_autoscaling as autoscaling, aws_elasticloadbalancingv2 as elbv2, aws_backup as backup, aws_events as events, aws_rds as rds)
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_cloudwatch as cloudwatch
from constructs import Construct
import aws_cdk.aws_certificatemanager as acm
from project_v1_1.config import *


class Deploy_Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

    #################################
    # Setting up the VPCs & Peering #
    #################################

    # WebVPC:
        webvpc = ec2.Vpc(self, "WebServerVPC",
                            # 2 AZ, 2 subnets. 2 Public en 2 Isolated
                           max_azs=web_az,
                           ip_addresses=ec2.IpAddresses.cidr(web_vpc_cidr),
                           subnet_configuration=[ec2.SubnetConfiguration(
                               subnet_type=ec2.SubnetType.PUBLIC,
                               name="WebServer"
                               
                            ),
                            ec2.SubnetConfiguration(
                                subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                                name="Database",
                                ),
                           ],
                           )
        self.webvpc = webvpc


    # MGMT VPC:
        self.mgmtvpc = ec2.Vpc(self, "MGMTVPC",
                            # 1 AZ, 1 subnet
                           max_azs=mgmt_az,
                           ip_addresses=ec2.IpAddresses.cidr(mgmt_vpc_cidr),
                           subnet_configuration=[ec2.SubnetConfiguration(
                               subnet_type=ec2.SubnetType.PUBLIC,
                               name="MGMT",
                            ),
                           ],
                           nat_gateways=0,
        )
        mgmtvpc = self.mgmtvpc
    
    # VPC Peering:
        Peering_connection = ec2.CfnVPCPeeringConnection(self, "Cloud10VPCPeer",
            peer_vpc_id=self.mgmtvpc.vpc_id,
            vpc_id=self.webvpc.vpc_id,

    
        )

    ####################
    # Security Groups: #
    ####################

    # Create the Security Groups:

        # Management Server:
        mgmt_sg=ec2.SecurityGroup(self, "MGMTSG",
                                    vpc=self.mgmtvpc,
                                    allow_all_outbound=False,)

        # Webserver:
        WS_SG = ec2.SecurityGroup(self, "WebServerSG",
                                 vpc=webvpc,
                                 allow_all_outbound=False
        )

        # Database:
        db_sg = ec2.SecurityGroup(self, "DatabaseSG",
                                 vpc=webvpc,
                                 allow_all_outbound=False
                                 )

        # Load Balancer:
        ws_lb_sg = ec2.SecurityGroup(self, "WebServerLoadBalancerSG",
                                 vpc=webvpc,
                                 allow_all_outbound=False
                                 )

    # Add Rules:
        ## Management Server: ##

        # RDP Access from Trusted Office IP.   
        mgmt_sg.add_ingress_rule(
                                ec2.Peer.ipv4(office_ip),
                                ec2.Port.tcp(3389), "OfficeIP"
                                )                       

        # RDP Access from Trusted Home IP.   
        mgmt_sg.add_ingress_rule(
                                ec2.Peer.ipv4(home_ip),
                                ec2.Port.tcp(3389), "HomeIP"
                                )  

        # SSH Access from office IP:
        mgmt_sg.add_ingress_rule(  
                                ec2.Peer.ipv4(office_ip),
                                ec2.Port.tcp(22), "SSH Access from office IP"
        )

        # SSH Access from office IP:
        mgmt_sg.add_ingress_rule(  
                                ec2.Peer.ipv4(home_ip),
                                ec2.Port.tcp(22), "SSH Access from office IP"

        )
    
        # SSH Access to everyone:
        mgmt_sg.add_egress_rule(
                                ec2.Peer.any_ipv4(), 
                                ec2.Port.tcp(22), "SSH Access to ANY IP"
        )      
        # HTTP Access to all
        mgmt_sg.add_egress_rule(
                                ec2.Peer.any_ipv4(), 
                                ec2.Port.tcp(80), "HTTP Access to ANY IP"
        )
    
        #HTTPS Access to all:

        mgmt_sg.add_egress_rule(ec2.Peer.any_ipv4(),
                                ec2.Port.tcp(443), "HTTPS Access to ANY IP"
        )

    
        # Webserver: #
           
        WS_SG.connections.allow_from(
           mgmt_sg, ec2.Port.tcp(22), " Allow SSH from Management Server") 
        
        WS_SG.connections.allow_to_any_ipv4(
            ec2.Port.tcp(80), "Allow HTTP from Web Server to ALL"
        )

        WS_SG.connections.allow_to_any_ipv4(
            ec2.Port.tcp(443), "Allow HTTPS from Web Server to ALL"
        )
        
        # Allow Traffic to and from Database:
        WS_SG.connections.allow_to(db_sg, ec2.Port.tcp(3306), "Allow MySQL from Web Server to Database")
        WS_SG.connections.allow_from(db_sg, ec2.Port.tcp(3306), "Allow MySQL from Database to Web Server")
       
    
        
        # DATABASE #

        # Allow connection to and from Web Server:
        db_sg.connections.allow_from(WS_SG, ec2.Port.tcp(3306), "Allow MySQL from Web Server to Database")
        db_sg.connections.allow_to(WS_SG, ec2.Port.tcp(3306), "Allow MySQL from Database to Web Server")

        # Allow connection to and from Management Server:
        db_sg.connections.allow_to(mgmt_sg, ec2.Port.tcp(3306), "Allow MySQL from Database to Management Server")
        db_sg.connections.allow_from(mgmt_sg, ec2.Port.tcp(3306), "Allow MySQL from Management Server to Database")
    
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
            key_name="WebServerKey", # Imports the key pair. Make sure you create the key pair first!
            vpc=self.mgmtvpc,
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),  # Use public subnet
            user_data=ec2.UserData.custom(win_userdata),
            block_devices=[
                ec2.BlockDevice(
                    device_name="/dev/sda1",
                    volume=ec2.BlockDeviceVolume.ebs(
                        volume_size=volume_size_mgmt,
                        encrypted=True,
                        delete_on_termination=True,
                    )
                )],
            )

       
    # Output public IP of Management Server:
        CfnOutput(self, "MGMTServer IP:", value=mgmtserver_instance.instance_public_ip)

    
    # Webserver Autoscaling
        webserver_instance = autoscaling.AutoScalingGroup(
            self,
            "Webserver",
            vpc=webvpc,
            vpc_subnets=ec2.SubnetSelection(subnet_group_name="Database"),  # Use private isolated subnet
            security_group=WS_SG,
            instance_type = ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO),
            machine_image=ec2.MachineImage.generic_linux({"eu-central-1": AMI_image}),
            key_name="WebServerKey", # Imports the key pair. Make sure you create the key pair first!')
            min_capacity=min_capacity,
            max_capacity=max_capacity,
            health_check=autoscaling.HealthCheck.elb(grace=Duration.seconds(60)),
           
            

         )
        webserver_instance.scale_on_cpu_utilization(
            'CPU-watch',
            target_utilization_percent=80,
        )
        
           
    ################################
    # Load Balancer for Webserver: #
    ################################

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
                                                    target_type=elbv2.TargetType.INSTANCE,
                                                    targets=[webserver_instance],
                                                    health_check=elbv2.HealthCheck( 
                                                                                    port="80",
                                                                                    protocol=elbv2.Protocol.HTTP,
                                                                                    path="/",
                                                                                    timeout=Duration.seconds(5),
                                                                                    healthy_threshold_count=2,
                                                                                    unhealthy_threshold_count=6,
                                                                                    interval=Duration.seconds(10)
                                                    ))
    # Create a certificate
        certificate = acm.Certificate(self, "MyCertificate",
                    domain_name=domain_ws,
                    validation= acm.CertificateValidation.from_dns(hosted_zone=None)
        )



    # Link ELB to Web Server:
        

        listener = webserver_lb.add_listener("Listener", default_target_groups=[webserver_tg], 
                                                        protocol=elbv2.ApplicationProtocol.HTTPS,
                                                        port=443, 
                                                        certificates=[elbv2.ListenerCertificate(certificate_arn=certificate.certificate_arn)]
                                                        )


        listener.connections.allow_from_any_ipv4(
            ec2.Port.tcp(80), "Allow HTTP from All")
        
        listener.connections.allow_to_any_ipv4(
            ec2.Port.tcp(80), "Allow HTTP to All")

        listener.connections.allow_to_any_ipv4(
            ec2.Port.tcp(443), "Allow HTTPS to All")
        
 
    # Redirect HTTP to HTTPS: -> To make it work, change protocol of listener to HTTPS, and add certificate.
        webserver_lb.add_redirect(
                        source_protocol=elbv2.ApplicationProtocol.HTTP,
                        source_port=80,
                        target_protocol=elbv2.ApplicationProtocol.HTTPS,
                        target_port=443,
                        )   

    ################
    # Route Tables #
    ################
    
    # MGMT Server to VPC-Peering to webserver:
        mgmt_rt = ec2.CfnRoute(self, "MGMTRoute",
                                route_table_id=mgmtvpc.public_subnets[0].route_table.route_table_id,
                                destination_cidr_block=web_vpc_cidr,
                                vpc_peering_connection_id=Peering_connection.ref,
                                )
    # Webserver to VPC-Peering to MGMT Server:    
        webserver_rt = ec2.CfnRoute(self, "WebServerRoute",
                                route_table_id=webvpc.isolated_subnets[0].route_table.route_table_id,
                                destination_cidr_block=mgmt_vpc_cidr,
                                vpc_peering_connection_id=Peering_connection.ref,
                                )
        
        CfnOutput(self, "Office_Ip_Added_To_Trusted_List:", value=office_ip)
        CfnOutput(self, "Home_Ip_Added_To_Trusted_List:", value=home_ip)

    ###########
    # Backups #
    ###########

    # Create a backup plan for MGMT Server EBS Volume:
        backup_vault = backup.BackupVault(self, "Cloud10Backup",
                                        backup_vault_name="BackupVaultCloud10",
                                        removal_policy=cdk.RemovalPolicy.DESTROY
                                        )


        backup_plan = backup.BackupPlan(self, "MGMTBackupPlan",
                                        backup_plan_name="MGMTBackup",
                                        backup_vault=backup_vault,
                                        )
        backup_plan.add_selection("MGMTBackupSelection",
                                    resources=[backup.BackupResource.from_ec2_instance(mgmtserver_instance)],
                                    
                                    )
        backup_rule = backup_plan.add_rule(backup.BackupPlanRule(
                                            delete_after=Duration.days(7),
                                            start_window=Duration.minutes(60),
                                            completion_window=Duration.minutes(120),
                                            # Set time is in UTC! NL Summertime = UTC +2, Wintertime = UTC +1
                                            schedule_expression=events.Schedule.cron(
                                                minute="00",
                                                hour="22",))
                                                )
                                            
        
    ############
    # Database #
    ############

    # Add Aurora DB To Private_Isolated subnet on the webserver vpc:
        webserver_db = rds.ServerlessCluster(self, "WebServerDB",
                                                engine=rds.DatabaseClusterEngine.AURORA_MYSQL,
                                                vpc=webvpc,
                                                vpc_subnets=ec2.SubnetSelection(subnet_group_name="Database"),  # Use Database subnet
                                                security_groups=[db_sg],
                                                backup_retention=Duration.days(7),
                                                removal_policy=cdk.RemovalPolicy.SNAPSHOT,
        )