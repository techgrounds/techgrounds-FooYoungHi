# EC2
Een VM aanmaken en inloggen.

## Key-terms
### EC2:
Het systeem in AWS waar je virtual machines kan draaien.

## Opdracht
#### Opdracht 1:
- Navigeer naar het EC2 menu.
- Maak een VM aan met de volgende parameters:  
	AMI: Amazon Linux 2 AMI (HVM), SSD Volume Type  
    Instance type: t2.micro  
    Default network, no preference for subnet  
    Termination protection: enabled  
    User data:  
		#!/bin/bash  
		yum -y install httpd  
		systemctl enable httpd  
		systemctl start httpd  
		`echo '<html><h1>Hello From Your Web Server!</h1></html>' >   /var/www/html/index.html`  
		Root volume: general purpose SSD, Size: 8 GiB  
		New Security Group:    
		Name: Web server SG  
		 Rules: Allow SSH, HTTP and HTTPS from anywhere  
#### Opdracht 2:
- Wacht tot de status checks uit de inititiation phase zijn en je de server kan bereiken.
- Log in via SSH.
- Terminate the instance


### Gebruikte bronnen
Geen.

### Ervaren problemen
Geen.

### Resultaat
Ik heb de instance aangemaakt volgens de opgegeven parameters. De volgorde in de opdracht was iets anders dan ik op mijn scherm zag, maar alles was te vinden. Ook het ik de instance kunnen 'Terminaten', door eerst de beveiliging uit te zetten.  
Screenshot staat in de 00_includes folder als [AWS-06-1.png](/00_includes/AWS-06-1.png).  
![](/00_includes/AWS-06-1.png)  
Bij de tweede opdracht heb ik in kunnen loggen.  
Screenshot staat in de 00_includes folder als [AWS-06-2.png](/00_includes/AWS-06-2.png).  
![](/00_includes/AWS-06-2.png)
