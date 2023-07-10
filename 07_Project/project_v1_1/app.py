#!/usr/bin/env python3
import os

import aws_cdk as cdk
# begin met je projectnaam. Daarna een punt gevolgd door de naam van je .py bestand, zonder extentie. 
# Na de 'import' zet je de naam van de class die je wilt importeren. 
from project_v1_1.pdscripts_stack import PDScripts_Stack
#from project_v1_1.fulldeploy_stack import Deploy_Stack
from project_v1_1.spaghetti_stack import Spaghetti_Stack
from project_v1_1.InstanceTemplate import EC2_Template






#from project_v1.spaghetti_stack import Spaghetti_Stack

deployment_region = cdk.Environment(
    account="835956440930", # Your AWS Account ID
    region="eu-central-1" # 
)



app = cdk.App()
# Hier geef je aan welke stack naam je wilt dat de classes hebben. Deze volgorde is ook de deploy --all volgorde!
#Deploy_Stack(app, "fulldeploy", env=deployment_region)
PDScripts_Stack(app, "bucket",)
Spaghetti_Stack(app, "spaghetti", env=deployment_region)
EC2_Template(app, "ec2template", env=deployment_region)
app.synth()
