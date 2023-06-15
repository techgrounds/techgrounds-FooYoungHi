import aws_cdk as core
import aws_cdk.assertions as assertions

from v1.0.v1.0_stack import V10Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in v1.0/v1.0_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = V10Stack(app, "v1-0")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
