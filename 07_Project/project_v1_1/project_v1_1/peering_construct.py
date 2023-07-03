import aws_cdk.aws_ec2 as ec2
from project_v1_1.VPC_construct import WebVPC_Construct, MGMTVPC_Construct
from constructs import Construct

class Peering_construct(Construct):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id)
        self.webvpc = WebVPC_Construct(self, 'webvpc').webvpc # WebServer VPC
        self.mgmtvpc = MGMTVPC_Construct(self, 'mgmtvpc').mgmtvpc # MGMT Server VPC

        self.peering_connection = ec2.CfnVPCPeeringConnection(self, "Cloud10VPCPeer",
            peer_vpc_id=self.mgmtvpc.vpc_id,
            vpc_id=self.webvpc.vpc_id,
        )
