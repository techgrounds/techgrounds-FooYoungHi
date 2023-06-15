import aws_cdk as core
import aws_cdk.assertions as assertions

from tg_project_10.tg_project_10_stack import TgProject10Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in tg_project_10/tg_project_10_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TgProject10Stack(app, "tg-project-10")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
