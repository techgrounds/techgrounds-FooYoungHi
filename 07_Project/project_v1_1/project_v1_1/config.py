import aws_cdk as cdk

##################################################
# Define the user data script for the WebServer: #
##################################################



user_data = """#!/bin/bash
             # Install Apache Web Server and PHP
             yum install -y httpd php
             # Turn on web server
             chkconfig httpd on
             service httpd start
             """