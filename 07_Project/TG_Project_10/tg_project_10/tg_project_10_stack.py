import aws_cdk as cdk
import aws_cdk.aws_s3 as s3
            
class PostDeploymentBucketStack(cdk.Stack):

    def __init__(self, scope: cdk.App, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
# Create Post Deployment Bucket
        bucket = s3.Bucket(self, "PostDeploymentBucket",
            bucket_name="post_deployment_bucket_cloud10", 
            versioned=True,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True)