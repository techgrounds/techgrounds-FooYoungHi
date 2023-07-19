import aws_cdk as cdk
import aws_cdk.aws_ec2 as ec2

# Change these BEFORE deployment:
deployment_region = cdk.Environment(
    account="<insert your account ID", # Your AWS Account ID
    region="eu-central-1" # The preferred region for your deployment
)
office_ip = "<insert IP>"               # Trusted IP from the Office
home_ip = "<insert IP"                  # Trusted IP from Home
AMI_image = "<insert AMI ID>"           # AMI ID for the WebServer
domain_ws = "<insert domain name>"      # Domain for your webserver certificate
key_name = "<insert key name>"          # Don't forget to create the key with te .sh file. Key name is caps sensitive.

# Change at own risk:

min_capacity = 1                        # Minimum number of EC2 instances to maintain
max_capacity = 3                        # Maximum number of EC2 instances to maintain
web_vpc_cidr = "10.10.10.0/24"          # CIDR block for the WebServer VPC
mgmt_vpc_cidr = "10.20.20.0/24"         # CIDR block for the Management VPC
web_az = 2                              # Amount of AZs in WebVPC
mgmt_az = 1                             # Amount of AZs in MGMTVPC
volume_size_web = 8                     # Size of the EBS volume for the WebServer
volume_size_mgmt = 30                   # Size of the EBS volume for the MGMTServer

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
   
   # Disable IE ESC for Administrators
    $AdminKey = "HKLM:\SOFTWARE\Microsoft\Active Setup\Installed Components\{A509B1A7-37EF-4b3f-8CFC-4F3A74704073}"
    $AdminValueName = "IsInstalled"
    Set-ItemProperty -Path $AdminKey -Name $AdminValueName -Value 0

    # Disable IE ESC for Users
    $UserKey = "HKLM:\SOFTWARE\Microsoft\Active Setup\Installed Components\{A509B1A8-37EF-4b3f-8CFC-4F3A74704073}"
    $UserValueName = "IsInstalled"
    Set-ItemProperty -Path $UserKey -Name $UserValueName -Value 0

    # Restart Windows Explorer to apply the changes
    Stop-Process -Name explorer -Force
    Start-Sleep -Seconds 3
    Start-Process -FilePath explorer


    # Install Chocolatey
    Set-ExecutionPolicy Bypass -Scope Process -Force
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
    iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

    # Update the package list
    choco upgrade chocolatey -y

    # Install MySQL Workbench
    choco install mysql.workbench -y

    # Re-enable IE ESC for Administrators
    $AdminKey = "HKLM:\SOFTWARE\Microsoft\Active Setup\Installed Components\{A509B1A7-37EF-4b3f-8CFC-4F3A74704073}"
    $AdminValueName = "IsInstalled"
    Set-ItemProperty -Path $AdminKey -Name $AdminValueName -Value 1

    # Re-enable IE ESC for Users
    $UserKey = "HKLM:\SOFTWARE\Microsoft\Active Setup\Installed Components\{A509B1A8-37EF-4b3f-8CFC-4F3A74704073}"
    $UserValueName = "IsInstalled"
    Set-ItemProperty -Path $UserKey -Name $UserValueName -Value 1

    # Restart Windows Explorer to apply the changes
    Stop-Process -Name explorer -Force
    Start-Sleep -Seconds 3
    Start-Process -FilePath explorer
</powershell>
        """
