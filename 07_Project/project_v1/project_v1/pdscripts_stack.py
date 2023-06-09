import aws_cdk as cdk
import aws_cdk.aws_s3 as s3
            
class PDScripts_Stack(cdk.Stack):

    def __init__(self, scope: cdk.App, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "PDScriptsCloud10",
            bucket_name="postdeploymentcloud10", 
            versioned=True,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True)