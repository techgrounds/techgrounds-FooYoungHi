import aws_cdk.aws_ec2 as ec2
from aws_cdk import Stack
from constructs import Construct
from project_v1_1.config import volume_size_web




class EC2_Template(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Pre-load userdata:
        with open("./project_v1_1/user_data.sh") as f:
            self.user_data = f.read()

        webserver_instance = ec2.Instance(
                self, "WebServerTemplate",
                                    vpc=ec2.Vpc.from_lookup(self, "DefaultVPC", is_default=True),
                                    instance_name="WebServerTemplate",
                                    instance_type=ec2.InstanceType('t3.nano'),
                                    machine_image=ec2.MachineImage.latest_amazon_linux2(),
                                    key_name="WebServerKey", # Imports the key pair. Make sure you create the key pair first!')
                                    user_data= ec2.UserData.custom(self.user_data),
                                    block_devices=[
                                        ec2.BlockDevice(
                                            device_name='/dev/xvda',
                                            volume=ec2.BlockDeviceVolume.ebs(
                                                volume_size=volume_size_web,
                                                encrypted=True,
                                            ))
                                    ]
                                    )