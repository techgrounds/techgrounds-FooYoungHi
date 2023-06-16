#!/usr/bin/env python3
import os

import aws_cdk as cdk
# begin met je projectnaam. Daarna een punt gevolgd door de naam van je .py bestand, zonder extentie. 
# Na de 'import' zet je de naam van de class die je wilt importeren. 
from project_v1.pdscripts_stack import PDScripts_Stack
from project_v1.network_stack import Network_Stack

app = cdk.App()
# Hier geef je aan welke stack naam je wilt dat de classes hebben. 
PDScripts_Stack(app, "bucket",
    )
Network_Stack(app, "network", )
app.synth()
