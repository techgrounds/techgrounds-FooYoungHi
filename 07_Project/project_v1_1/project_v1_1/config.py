import aws_cdk as cdk
import aws_cdk.aws_ec2 as ec2

# Region & Account:
deployment_region = cdk.Environment(
    account="835956440930", # Your AWS Account ID
    region="eu-central-1" # The preferred region for your deployment
)

# Change these BEFORE deployment:
office_ip = "193.32.249.135/32"         # Trusted IP from the Office
home_ip = "192.169.2.1/32"              # Trusted IP from Home
AMI_image = "ami-01bdc1b8d0dad4cd8"     # AMI ID for the WebServer
domain_ws = "cloud10.dannystammers.nl"  # Domain for your webserver certificate


# Change at own risk:

min_capacity = 1 # Minimum number of EC2 instances to maintain
max_capacity = 3 # Maximum number of EC2 instances to maintain
web_vpc_cidr = "10.10.10.0/24" # CIDR block for the WebServer VPC
mgmt_vpc_cidr = "10.20.20.0/24" # CIDR block for the Management VPC
web_az = 2 # Amount of AZs in WebVPC
mgmt_az = 1 # Amount of AZs in MGMTVPC
volume_size_web = 8 # Size of the EBS volume for the WebServer
volume_size_mgmt = 30 # Size of the EBS volume for the MGMTServer

win_userdata = """
<powershell>
    # Install OpenSSH
    Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
    
    # Start the sshd service
    Start-Service sshd
    
    # Set the sshd service to start automatically
    Set-Service -Name sshd -StartupType Automatic
    
    # Confirm that the firewall rule is configured
    Get-NetFirewallRule -Name *ssh*
    
    # If the firewall rule is not configured, run the following command
    New-NetFirewallRule -Name sshd -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
    </powershell>
    """
