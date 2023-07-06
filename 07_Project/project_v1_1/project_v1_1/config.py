import aws_cdk as cdk
import aws_cdk.aws_ec2 as ec2

# Define the user data script for the WebServer:

min_capacity = 1 # Minimum number of EC2 instances to maintain
max_capacity = 3 # Maximum number of EC2 instances to maintain
web_vpc_cidr = "10.10.10.0/24" # CIDR block for the WebServer VPC
mgmt_vpc_cidr = "10.20.20.0/24" # CIDR block for the Management VPC
web_az = 2 # Amount of AZs in WebVPC
mgmt_az = 1 # Amount of AZs in MGMTVPC
volume_size_web = 8 # Size of the EBS volume for the WebServer
volume_size_mgmt = 8 # Size of the EBS volume for the MGMTServer
