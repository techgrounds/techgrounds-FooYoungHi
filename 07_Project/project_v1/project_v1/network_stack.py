from aws_cdk import CfnOutput, Stack
import aws_cdk.aws_ec2 as ec2
from constructs import Construct
            
class Network_Stack(Stack):

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
        CfnOutput(self, "Output",
                       value=self.vpc.vpc_id)