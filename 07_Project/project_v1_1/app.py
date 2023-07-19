#!/usr/bin/env python3
import os
import aws_cdk as cdk
# begin met je projectnaam. Daarna een punt gevolgd door de naam van je .py bestand, zonder extentie. 
# Na de 'import' zet je de naam van de class die je wilt importeren. 
from project_v1_1.fulldeploy_stack import Deploy_Stack
from project_v1_1.InstanceTemplate import WS_Template
from project_v1_1.config import deployment_region


app = cdk.App()
# Hier geef je aan welke stack naam je wilt dat de classes hebben. Voor deployment, deploy enkel de fulldeployment!
Deploy_Stack(app, "cloud10project", env=deployment_region)
WS_Template(app, "wstemplate", env=deployment_region)
app.synth()
