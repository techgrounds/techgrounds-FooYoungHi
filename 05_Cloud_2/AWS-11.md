# Elastic Load Balancing & Auto Scaling
Werken met de load balancer en met auto scaling.

## Key-terms
#### Elastic Load Balancer:
In feite gewoon een *Load Balancer*, maar dan een die meeschaalt met de traffic die er van wordt gevraagd.  
Een *Load Balancer* zorgt er voor dat dataverkeer wordt verdeeld over meerdere apparaten, om te voorkomen dat 1 apparaat een te zware load heeft, terwijl een andere niets aan het doen is. Dit kan gaan om netwerkapparatuur, maar ook om VMs die bijvoorbeeld een webserver draaien.  
Het voordeel hiervan is dat je de apparatuur kan uitbreiden, zonder dat de user daar iets van merkt. Ook heb je, als er bijvoorbeeld een VM vastloopt, of hardware defect raakt, geen onderbreking, omdat het dataverkeer wordt omgeleid naar een apparaat dat wel werkt.  
Het is een vorm van redundancy, omdat je niet afhankelijk bent van 1 apparaat of software.  

AWS maakt onderscheid tussen 4 soorten Load Balancer:
- **Application Load Balancer, ALB:**
	Dit is een Layer 7 Load Balancer. Het kan bijvoorbeeld meerdere HTTP instances aan over meerdere apparaten (target groups). Het kan ook meerdere applicaties managen op dezelfde machine, zoals containers.
-  **Network Load Balancer, NLB:**
	Deze load balancer werkt op het TCP niveau (Layer 4), het zorgt voor snellere traffic in het netwerk.
- **Gateway Load Balancer:**
	Dit is een load balancer specifiek voor Gateways. Het werkt op Layer 3. Dit zorgt er voor dat niet alle data door 1 gateway hoeft, maar verdeeld wordt om een bottleneck te voorkomen.
- **Classic Load Balancer:**
	Dit is een verouderde, algemene load balancer. Het gebruik van deze LB wordt door AWS afgeraden en ontmoedigd. Het gaat over Layer 7 en 4. Deze LB is vervangen door de ALB en NLB, die veel 'slimmer' zijn en veel gespecializeerder in hun taak.
	
#### Auto Scaling:
Een onderdeel van EC2 waarbij je in combinatie met een load balancer het aantal instances kan aanpassen aan de load die noodzakelijk is op dat moment. Als er veel vraag is, dan maakt hij extra instances aan, en als de load weer 'normaal' is, dan haalt hij die extra instances weer weg.

#### Launch Config:
Verouderd systeem.
Dit is een template waarin je aangeeft op welke manier je een image wil aanmaken, zodat je niet steeds dezelfde stappen moet doornemen als je vaak dezelfde instance nodig hebt.

#### Launch Template:
Vergelijkbaar met een *Launch config*, maar dan met meer opties en betere controlemogelijkheden.

## Opdracht

### Oefening 1:
- Maak een instance aan met de volgende vereisten:
	- Region: Frankfurt (eu-central-1)
	- AMI: Amazon Linux 2
	- Type: t3.micro
	- User Data:
			```#!/bin/bash
			# Install Apache Web Server and PHP
			yum install -y httpd mysql php
			# Download Lab files
			wget [https://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-RESTRT-1/80-lab-vpc-web-server/lab-app.zip](https://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-RESTRT-1/80-lab-vpc-web-server/lab-app.zip)
			unzip lab-app.zip -d /var/www/html/
			# Turn on web server
			chkconfig httpd on
			service httpd start```
	- Security Group: Allow HTTP
- Wacht tot de security checks klaar zijn.
- Maak een AMI Image van je instance met de naam: 'Web Server AMI'.

### Oefening 2:
- Maak een *Application Load Balancer* met de volgende vereisten:
	- Naam: LabELB
	- Listener: HTTP op port 80
	- AZs: eu-central-1a en eu-central-1b
	- Subnets moeten publiek zijn.
	- Security Group:
		- Naam: ELB SG
		- Rules: Allow HTTP
	- Target Group:
		- Name: LabTargetGroup
		- Targets: Gemaakt door de autoscaler

### Oefening 3:
- Maak een *Launch configuration* voor de *Auto scaling group*. Het moet identiek zijn aan de server die al draait.
- Maak een Auto Scale Group met de volgende vereisten:
	- Naam: Lab ASG
	- Launch Configuration: Web Server Launch Configuration
	- Subnets: Moeten in eu-central-1a en eu-central-1b zitten.
	- Load Balancer: LabELB
	- *Group metrics collection in Cloud Watch* moet aan staan.
	- Group size:
		- Desired capacity: 2
		- Minimum capacity: 2
		- Maximum capacity: 4
	- Scaling policy: Target Tracking met een target van 60% CPU

### Oefening 4:
- Verifiëer dat de instances online zijn en dat ze onderdeel zijn van de target group van de load balancer.
- Maak verbinding met de ELB via de DNS naam van de ELB.
- Voer een load test uit op de server(s) via de website die je ziet. Bekijk wat er gebeurt.

### Gebruikte bronnen


### Ervaren problemen
Ik liep tegen 2 problemen op: De autoscaler vond het noodzakelijk  om de *desired instances* op 4 te zetten, terwijl ik 2 had ingesteld. Dit had ik weer teruggedraaid in de settings. Na verder lezen had ik begrepen dat dit niet noodzakelijk is, omdat dit bij het aanmaken ging om het start aantal instances, en dat het automatisch aanpassen te maken heeft met het aantal instances dat noodzakelijk is. De term *desired* is dus niet het aantal instances dat mijn voorkeur heeft, maar het aantal instances dat op dat moment gewenst is.
Het tweede probleem ging om het niet downscalen. Na veel zoeken ben ik er achter gekomen dat ik in de settings van de autoscaler de *suspended processes* het *Terminate* command had geblokkeerd. Ik dacht dat ik hier de actie voor het downscalen moest aangeven, maar ik had niet goed gelezen. De autoscaler wilde dus de overbodige instances *terminaten*, maar ik had handmatig dat proces geblokkeerd. Nadat ik dit had gezien en aangepast, waren de overbodige 2 instances snel automatisch geterminate.

### Resultaat
#### Oefening 1:
De EC2 instance is aangemaakt en via het Actions menu heb ik een AMI gemaakt.
Screenshot staat in de 00_includes folder als [AWS-11-1.png](/00_includes/AWS-11-1.png).  
![](/00_includes/AWS-11-1.png)  

#### Oefening 2:
De Load Balancer is aangemaakt, samen met de SG en TG.
Screenshot staat in de 00_includes folder als [AWS-11-2.png](/00_includes/AWS-11-2.png).  
![](/00_includes/AWS-11-2.png)  

#### Oefening 3:
Ik heb er voor gekozen om een *Launch Template* aan te maken in plaats van een *Launch Configuration*, aangezien ik had begrepen dat de Launch Configurations uitgefaseerd worden ter faveure van de Templates. Het leek mij handiger om dan de nieuwe methode te leren.  
Ik heb ook de autoscaler aangemaakt.  
Screenshot staat in de 00_includes folder als [AWS-11-3.png](/00_includes/AWS-11-3.png).  
![](/00_includes/AWS-11-3.png)  

#### Oefening 4:
Ik heb een load test gestart op beide servers. Het upscalen ging zoals aangegeven. Nadat de load test was gestopt, waren de overbodige instances vanzelf afgebouwd.  
Screenshots staat in de 00_includes folder als [AWS-11-4.png](/00_includes/AWS-11-4.png) en [AWS-11-5.png](/00_includes/AWS-11-5.png).  
![](/00_includes/AWS-11-4.png)  
![](/00_includes/AWS-11-5.png)  
