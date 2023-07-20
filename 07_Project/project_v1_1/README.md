# Hoe deploy en configureer je dit project:

## Stappen vóór deployment:
Zorg er voor dat het systeem waar de deployment plaats vindt alle nodige software heeft geïnstalleerd, waaronder AWS CLI en CDKv2, en importeer het project.


## Key pair aanmaken voor SSH toegang:
Maak een key pair aan met keypair.sh, die in dezelfde folder staat als dit document. Vergeet niet eerst het bestand te openen met een text-editor en de naam van de keypair in te vullen. Het private-key.pem bestand wordt opgeslagen in de map waar het script is uitgevoerd.
![](/00_includes/project/KeyPair.png)


## Webserver Image aanmaken:

Deploy eerst InstanceTemplate.py, om de webserver aan te maken waar een image van gemaakt dient te worden:
`cdk deploy wstemplate`.

Dit deployt een Amazon Linux EC2 instance die httpd, php en MariaDB installeert. Tevens installeert het een testpagina waar de load balancer en autoscaling getest kan worden.

Optioneel is te testen of alles werkt door de public IP van de image te plakken in de adresbalk.

Om de AMI image aan te maken, gebruik de informatie in de onderstaande link.
[Image aanmaken - AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html)
De instance staat goed geconfigureerd, dus andere instellingen zijn niet nodig.

Wanneer de image is aangemaakt, kopiëer de AMI ID van de nieuwe image en zet deze in config.py onder AMI_image.

Nu kan de gemaakte image worden verwijderd met:
`cdk destroy wstemplate`.

## Deployment stack:

*Voordat* de stack gedeployd wordt, moet in config.py nog een aantal waardes van variables naar wens worden ingevuld:
![](/00_includes/project/BeforeDeploySettings.png)


Deploy de stack met `cdk deploy fulldeploy'

In de console bij de AWS Certificate Manager is een nieuw certificaat aangemaakt voor het opgegeven (sub)domein. De deployment blijft hangen tot deze certificaat is geaccepteerd. Hiervoor moet bij de domain registrar de CNAME values worden aangepast naar de aangegeven waardes van het certificaat. Deze zijn te vinden als je op het certificaat klikt. De exacte format hangt af van de registrar. De toekenning van het certificaat kán een flinke tijd duren. Tot die tijd blijft de deploy hier op wachten.

## Post Deployment:

### Management server:

#### RDP toegang krijgen:
Om toegang te krijgen via RDP is het IP adres van de instance nodig en het wachtwoord.
Het IP adres is te vinden in de output na de deploy als "MGMTServerIP". Het wachtwoord is helaas alleen op te halen in de console, deze wordt om veiligheidsredenen niet via de CDK gegeven.
De instructies zijn [hier](https://repost.aws/knowledge-center/retrieve-windows-admin-password) te vinden.
Belangrijk om te weten is dat toegang tot de management server alleen toegankelijk is via de opgegeven IP adressen in config.py.

#### Windows userdata verifiëren:
Het is verstandig om eerst de management (windows) server te benaderen om te kijken of alle userdata goed is geïnstalleerd. Helaas wil de installatie van mysql workbench nog wel eens falen. Als dit het geval blijkt te zijn, kopiëer de userdata uit config.py en plak deze in de powershell van de instance. Soms vergt het een aantal pogingen voordat myqsl.workbench wil installeren. Uiteraard kan handmatig downloaden en installeren ook, indien rekening gehouden wordt met de strenge beveiliging van IE Enhanced Security Configuration.


### Webserver:

#### SSH verbinding met de webserver:
De webserver is via SSH alleen te benaderen via de Management server als bastion host. In Linux is de .pem file toe te voegen aan de keychain met het volgende command:
`ssh-add <keyname>.pem`
Voor andere operating systems zijn vergelijkbare opties mogelijk.
Om de jump te maken via de management server gebruik
`ssh -J Administrator@<mgmtserverip> ec2-user@<webserverip>`
Hierbij is 'Administrator' de standaard username van de Windows Server instance en 'ec2-user' de standaard username van de linux instance.


## Database:

De endpoint (hostname) van de database is te achterhalen door middel van deze command:
`aws rds describe-db-clusters --query '*[].{Endpoint:Endpoint,ReaderEndpoint:ReaderEndpoint,CustomEndpoints:CustomEndpoints}'`
In de output staat de endpoint.
Het wachtwoord is te vinden in de secrets manager in de console.
De username is standaard 'admin'.

### Windows:
Om verbinding te maken met de database in windows is mysql workbench geïnstalleerd. Bij het aanmaken van een nieuwe verbinding is de hostname de 'endpoint' van de database instance. 

### Linux:
In Linux maak je verbinding met de database via
`mysql -h <endpoint> -P 3306 -u admin -p`