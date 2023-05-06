# Files,Elastic Beanstalk,Cloudfront,Route53, Database


## Key-terms

### Elastic Beanstalk:

AWS heeft meer dan honderd services, met veel configuratiemogelijkheden en functionaliteit. Het is hierdoor echter een uitdaging om alles precies zo in te stellen als jij wilt wanneer je complexe dingen gaat doen.  
Voor mensen en organisaties die niet de expertise of tijd hebt om dit te managen, is Elastic Beanstalk ontworpen.  
Deze service zorgt op de achtergrond voor het detailwerk, zodat de gebruiker zich kan richten op de applicaties die ze draaien. De gebruiker hoeft geen kennis te hebben van de onderliggende infrastructuur. Het enige dat je hoeft te doen is je applicatie te uploaden en AWS zorgt voor de rest.
EB Ondersteunt applicaties die ontwikkeld zijn in *Go, Java, .NET, Node.js, PHP, Python, en Ruby.*
Je betaalt niet extra voor de service, je betaalt alleen voor de gebruikte resources.

### Cloudfront:
Dit is een service die er voor zorgt dat de data die je deelt op de meest efficiënt mogelijke manier bij de gebruiker aankomt. Dit gebeurt door middel van *Edge Locations* wereldwijd. Je host je content in je eigen omgeving, zoals een S3 bucket of webserver, en Cloudfront zorgt er voor dat deze content lokaal bij de gebruiker op een *Edge Location* staat, zodat de latency laag blijft.

### Route 53:
De DNS server van AWS.

### Elastic File System, EFS:
Zie dit als een network drive. Het hoeft niet gekoppeld te zijn aan een instance, zoals EBS, en is niet noodzakelijk gebonden aan één AZ. Het is toegankelijk van uit de hele region, als je dit zo instelt. Je kan het instellen binnen 1 AZ, dit is goedkoper.  
Het is ook toegankelijk (mountable) via een *on premise* apparaat.  

EFS is niet een vaste grootte; het groeit mee met wat er op staat. Zo betaal je alleen voor wat je gebruikt. Je hoeft ook geen start-grootte aan te geven, alles gaat vanzelf.  

### RDS/Aurora:
RDS staat voor *Relational Database.*  
Aurora is een RDS speciaal gemaakt voor de AWS infrastructuur, zodat het zo snel en efficiënt mogelijk functioneert.  
Aurora is een op zichzelf staande service, die niet vast hoeft te zitten aan een EC2 instance of iets anders.  
Bij het aanmaken kan de gebruiken kiezen om het op een zelf onderhouden server te draaien, of *serverless*, waarbij AWS ervoor zorgt dat het allemaal blijft werken.

## Opdracht
Bestudeer:
 - Elastic Beanstalk
 - Cloudfront
 - Route 53

Krijg practische vervaring met:
- EFS
- RDS/Aurora

### Gebruikte bronnen
[Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)  
[Cloudfront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)  
[Route 53]()  
[EFS](https://www.youtube.com/watch?v=Aux37Nwe5nc)  
[EFS vs EBS vs S3](https://www.youtube.com/watch?v=6vNC_BCqFmI&t=1087s&pp=ygUKZWZzIHZzIGVicw%3D%3D)  


### Ervaren problemen
Het duurde veel te lang om door te hebben wat de Elastic Beanstalk was, waardoor er veel tijd verloren ging. Ik heb nu een redelijk idee van wat het is, maar wil er nog meer over te weten komen om een goed begrip te hebben.  
Ook had ik ruzie met het aanmaken en verbinden met Aurora, al had ik op de dag waar ik het probeerde ernstige concentratieproblemen. De volgende dag lukte het zonder problemen.

### Resultaat
#### EFS: 
Ik heb me verdiept in EFS, gekeken wat het verschil is met *EBS* en *S3* een EFS aangemaakt in mijn omgeving. Ik heb hem niet gemount in een EC2 instance, omdat dit hetzelfde gaat als EBS en ik dit al meerdere keren heb gedaan. Het is voor mij dus geen toegevoegde waarde.  
Screenshot staat in de 00_includes folder als [AWS-13-1.png](/00_includes/AWS-13-1.png).  
![](/00_includes/AWS-13-1.png)  

#### Aurora:
Ik heb me verdiept in Aurora, snap wat het is en doet. Ik heb een instance aangemaakt en hiermee verbonden. Hiervoor heb ik de [Getting Started Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.Aurora.html) van AWS gebruikt.  
Screenshot staat in de 00_includes folder als [AWS-13-2.png](/00_includes/AWS-13-2.png).  
![](/00_includes/AWS-13-2.png)  
