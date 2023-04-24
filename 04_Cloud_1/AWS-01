# AWS Global Infrastructure
Kennis maken met AWS

## Key-terms

### Region:
Elke regio is een afzonderlijke geografische locatie.
Binnen een region kunnen meerdere availability zones zitten.
Elke regio is ontworpen on los te staan van de andere Regions, vanwege stabiliteit.

### AWS Availability Zone (AZ):
Een lokatie binnen een region waar een Datacenter staat.
Er kunnen per Region meerdere AZs zijn.

### Edge Location:
"**A site that CloudFront uses to cache copies of your content for faster delivery to users at any location.**"
Simpel gezegd: Dit is een locatie waar jouw data naartoe wordt gekopieerd om er voor te zorgen dat de content overal te wereld snel bereikbaar is. Dit zijn geen complete datacenters. Dit wordt gedaan door de Amazon Services *Cloudfront* en *Route 53*, de DNS oplossing.


## Opdracht
- Wat is een AWS Availability Zone?
- Wat is een region?
- Wat is een Egde Account?
- Waarom zou je een bepaalde regio kiezen? Bijvoorbeeld Frankfurt over Oregon?

### Gebruikte bronnen
[AZ & Zones:](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)  
[Regions:](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-region.html)

### Ervaren problemen
Geen.

### Resultaat
Antwoord op vraag:  
- Waarom zou je een bepaalde regio kiezen? Bijvoorbeeld Frankfurt over Oregon?

Dit kan gaan om latency; hoe verder de AZ bij jouw locatie vandaan, hoe hoger de latency. Ook kunnen de kosten verschillen, aangezien *cross-region data transfer fees* een ding zijn. Daarnaast kunnen er wetten zijn die data in een bepaalde regio moeten hebben.
AWS heeft ook allerlei beveiligingsmaatregelen genomen, zoals het aanmaken van  een *EC2 keypair* voor een cluster, wat in dezelfde regio moet worden aangemaakt als waar de cluster zich bevind.  
Ook zijn sommige functies alleen beschikbaar in een bepaalde regio.
