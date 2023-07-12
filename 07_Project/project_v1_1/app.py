#!/usr/bin/env python3
import os
import aws_cdk as cdk
# begin met je projectnaam. Daarna een punt gevolgd door de naam van je .py bestand, zonder extentie. 
# Na de 'import' zet je de naam van de class die je wilt importeren. 
from project_v1_1.pdscripts_stack import PDScripts_Stack
from project_v1_1.spaghetti_stack import Spaghetti_Stack
from project_v1_1.fulldeploy_stack import Deploy_Stack
from project_v1_1.InstanceTemplate import EC2_Template
from project_v1_1.config import deployment_region


app = cdk.App()
# Hier geef je aan welke stack naam je wilt dat de classes hebben. Voor deployment, deploy enkel de fulldeployment!
PDScripts_Stack(app, "bucket",)
Deploy_Stack(app, "fulldeploy", env=deployment_region)
Spaghetti_Stack(app, "spaghetti", env=deployment_region)
EC2_Template(app, "ec2template", env=deployment_region)
app.synth()
