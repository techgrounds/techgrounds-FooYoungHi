# Virtual Private Cloud, VPC
Een VPC opzetten met meerdere subnets en security rules.

## Key-terms

### Virtual Private Cloud, VPC:
Een virtueel 'bedrijfsnetwerk'. In een VPC kan je het netwerk onderverdelen in subnetten, kan je Security groups (firewalls) toevoegen etc. etc.

### Elastic IP:
Een *static IP* die je kan gebruiken om aan een EC2 instance te koppelen. Zonder een Elastic IP krijgt de EC2 instance elke keer dat hij opnieuw opstart een ander IP adres. Hiermee kan je ook heel snel overschakelen op een andere instance, als er iets mis gaat, door de IP te remappen naar de backup instance.

## Opdracht
### Deel 1:
- Wijs een *Elastic IP* toe aan je account.
- Maak een VPC met de volgende vereisten:
	- Region: Frankfurt (eu-central-1)
       - VPC with a public and a private subnet
	-  Name: Lab VPC
	-  CIDR: 10.0.0.0/16
- Vereisten public subnet:
	- Name: Public subnet 1
	- CIDR: 10.0.0.0/24
	- AZ: eu-central-1a
- Vereisten private subet:
	- Name: Public subnet 1
	- CIDR: 10.0.0.0/24
	- AZ: eu-central-1a

### Deel 2:
- Maak nog een public subnet met de volgende vereisten:
	- VPC: Lab VPC
	- Name: Public Subnet 2
	- AZ: eu-central-1b
	- CIDR: 10.0.2.0/24
- Maak nog een private subnet met de volgende verseisten:
	- VPC: Lab VPC
	- Name: Private Subnet 2
	- AZ: eu-central-1b
	- CIDR: 10.0.3.0/24
- Kijk in de *main route table* van **Lab VPC**. Daar moet je de NAT Gateway zien. Hernoem deze naar *Private Route Table*.
- Voeg beide *private subnets* toe aan deze route table als *Explicit Associate*.
- Kijk naar de andere route table, deze moet de internet gateway hebben. Hernoem deze naar *Public Route Table*.
- Voeg beide *public subnets* toe aan deze route table als *Explicit Associate*.

### Deel 3:
- Maak een security group aan met de volgende vereisten:
	- Name: Web SG
	- Description: Enable HTTP Access
	- VPC: Lab VPC
	- Inbound rule: allow HTTP access from anywhere
	- Outbound rule: Allow all traffic

### Deel 4:
- Launch een EC2 instance met de volgende vereisten:
	- AMI: Amazon Linux 2
	- Type: t3.micro
	- Subnet: Public subnet 2
	- Auto-assign Public IP: Enable
	- User data:  
			```#!/bin/bash  
			 # Install Apache Web Server and PHP  
			yum install -y httpd mysql php  
			# Download Lab files  
			wget https://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-RESTRT-1/80-lab-vpc-web-server/lab-app.zip  
			unzip lab-app.zip -d /var/www/html/  
			# Turn on web server  
			chkconfig httpd on  
			service httpd start```  

	- Tag:
	- Key: Name
	- Value: Web server
	- Security Group: Web SG
	- Key pair: no key pair
- Verbindt met de instance via de public IPv4 DNS name.


### Gebruikte bronnen
[Elastic IP](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html)

### Ervaren problemen
Het duurde even voordat ik doorhad hoe je de subnetten kon aanpassen, maar daarna ging het voorspoedig. Het enige waar ik tegen aanliep was bij de routing tables. Volgens de opdracht zouden er 2 moeten zijn, maar ik zie er 3.

### Resultaat
#### Deel 1:
De VPC is aangemaakt.  
Screenshot staat in de 00_includes folder als [AWS-10-1.png](/00_includes/AWS-10-1.png).  
![AWS-10-1.png](/00_includes/AWS-10-1.png)  

#### Deel 2:
De extra subnets zijn aangemaakt.  
Screenshot staat in de 00_includes folder als [AWS-10-2.png](/00_includes/AWS-10-2.png).  
![AWS-10-2.png](/00_includes/AWS-10-2.png)  
De private subnets zijn in de *private subnet* routing table gezet.  
Screenshot staat in de 00_includes folder als [AWS-10-3.png](/00_includes/AWS-10-3.png).  
![AWS-10-3.png](/00_includes/AWS-10-3.png)  

De public subnets in de *public subnet*.  
Screenshot staat in de 00_includes folder als [AWS-10-4.png](/00_includes/AWS-10-4.png).  
![AWS-10-4.png](/00_includes/AWS-10-4.png)  


#### Deel 3:
De Security Group is aangemaakt.
Screenshot staat in de 00_includes folder als [AWS-10-5.png](/00_includes/AWS-10-5.png).  
![AWS-10-5.png](/00_includes/AWS-10-5.png)  

#### Deel 4:
De instance is aangemaakt en de koppelingen aan de Security group en VPC zijn gemaakt. Verbinding kunnen maken via de public IPv4 DNS name.  
Screenshot staat in de 00_includes folder als [AWS-10-6.png](/00_includes/AWS-10-6.png).  
![AWS-10-6.png](/00_includes/AWS-10-6.png)  
