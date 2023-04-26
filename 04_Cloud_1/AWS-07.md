# Elastic Block Store, EBS
Leren werken met EBS.

## Key-terms
### EBS:
*Elastic Block Store*.  
Dit is het systeem in AWS waarmee je drives kan toevoegen aan je VM.

## Opdracht
#### Deel 1:
- Navigeer naar het EC2 menu
- Maak een t2.micro Amazon Linux 2 machine met alle standaard settings.
- Maak een nieuwe EBS volume aan met de volgende eisen:
	Volume type: General Purpose SSD (gp3)
    Size: 1 GiB
    Availability Zone: same as your EC2
- Wacht tot de status 'available' is.

#### Deel 2:
- Verbind je nieuwe EBS volume aan je EC2 instance.
- Verbind met je EC2 instance via SSH.
- Mount het EBS volume in je instance.
- Maak een tekstbestand en sla deze op naar de EBS.

#### Deel 3:
- Maak een snapshot van je EBS volume.
- Haal het tekstbestand van je eerste EBS volume.
- Maak een nieuwe volume aan via je snapshot.
- Detach je eerste EBS volume.
- Attach je nieuwe EBS volume en mount deze.
- Zoek je tekstbestand op de nieuwe EBS.

### Gebruikte bronnen
[Disk mounten:](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html)  
[Fdisk](https://linuxhint.com/use-fdisk-format-partition/)  

### Ervaren problemen
Ik liep tegen 3 dingen aan:  
1) Eerst had ik de volledige default settings gedaan, zoals in de opdracht staat, maar dan maakt AWS geen keypair aan en koppelt hij het niet aan een bestaande keypair. Hiermee moet je dus via een enórme omweg in de instance een keypair aanmaken. Dit viel dusdanig buiten de opdracht, dat ik de instance had 'geterminate' en een nieuwe had aangemaakt.
2) Ik ging er van uit dat de EBS standaard dezelfde AZ had als mijn instance, maar bleek dat ik die moest kiezen in een dropdown menu.
3) Bij het mounten van de drive liep ik tegen problemen op; hij weigerde te mounten. Ik had op de EBS volume een nieuwe partitie aangemaakt via fdisk en een xfs FS gegeven. Via `lsblk -f` kon ik wel zien dat hij een FS had. Na de instance een reboot te hebben gegeven, wilde hij ineens wel mounten.

### Resultaat
#### Deel 1:
De nieuwe EC2 instance is aangezet en de EBS is aangemaakt.  
Screenshots staan in de 00_includes folder als [AWS-07-1.png](/00_includes/AWS-07-1.png) en [AWS-07-2.png](/00_includes/AWS-07-2.png)  
![](/00_includes/AWS-07-1.png)  
![](/00_includes/AWS-07-2.png)  

#### Deel 2:
De EBS is gekoppeld aan de EC2 instance. Dit is gedaan door de volume te selecteren en dan bij actions 'attach' te kiezen.  
De drive is gemount in de instance en het tekstbestand is aangemaakt. Screenshot staat in de 00_includes folder als [AWS-07-3.png](/00_includes/AWS-07-3.png)  
![](/00_includes/AWS-07-3.png)  
#### Deel 3: 
Snapshot is gemaakt via het 'actions' menu in de EBS dashboard en het tekstbestand is verwijderd.  Screenshot staat in de 00_includes folder als [AWS-07-4.png](/00_includes/AWS-07-4.png).  
![](/00_includes/AWS-07-4.png)  
Van de snapshot heb ik een nieuwe volume aangemaakt. Dit is gedaan via het 'snapshots' menu bij EBS. Screenshot staat in de 00_includes folder als [AWS-07-5.png](/00_includes/AWS-07-5.png).  
![](/00_includes/AWS-07-5.png)  

Het 'oude' EBS volume was ontkoppeld, maar voordat dit werkte moest hij in Linux eerst unmounted worden. Daarna verdween hij uit de lijst.  
Na het koppelen van de nieuwe drive en deze gemount te hebben, was het textbestand weer aanwezig. Screenshot staat in de 00_includes folder als [AWS-07-6.png](/00_includes/AWS-07-6.png).  
![](/00_includes/AWS-07-6.png)  
