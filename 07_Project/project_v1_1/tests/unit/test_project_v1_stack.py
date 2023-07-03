import aws_cdk as core
import aws_cdk.assertions as assertions

from project_v1.project_v1_stack import ProjectV1Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in project_v1/project_v1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ProjectV1Stack(app, "project-v1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
