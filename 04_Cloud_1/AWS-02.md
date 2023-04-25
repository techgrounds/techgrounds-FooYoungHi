# AWS Pricing
Bekijken wat de gratis services zijn, wat de voordelen zijn van Cloud/AWS.

## Key-terms

### Total Cost of Ownership, TCO:
Dit wordt gebruikt om de kosten te berekenen van het 'traditioneel' hosten van je eigen infrastructuur. Hierbij wordt de 'capital expenditures', *capex* bekeken, en tegenover de 'operational (variale) expenditure', *opex* gezet.

### Vier voordelen van de AWS pricing model:

#### 1. Pay as you go:
Je betaalt alleen voor wat je gebruikt. Heb je bijvoorbeeld maar af en toe piekbelasting, dan hoef je niet, zoals bij self-hosted, een stevige server hebben draaien die constant resources aan het verspillen is wanneer deze kracht niet gebruikt wordt. Bij AWS (en Cloud in het algemeen), betaal je voor de opslag en rekenkracht die je daadwerkelijk gebruikt. Is er een piek? Dan schaalt de cloud zelf op tot een zelf ingestelde maximum.

#### 2. Pay less by using more:
In feite kan je dit zien als staffelkorting. Hoe meer storage je bijvoorbeeld gebruikt, hoe minder je per GB betaalt. De lagere prijzen gaan pas over de hogere tiers. Iedereent betaalt voor de eerste 50TB hetzelfde in dezelfde regio.

#### 3. Save when you reserve:
Als je voor 1-3 jaar 'beloofd' om bepaalde kosten te maken, kan je in aanmerking komen voor korting.

#### 4. Benefit from massive economies of scale:
Omdat AWS grootschalig inkoopt, zowel de hardware als dingen zoals electriciteit en deze kosten verdelen onder de klanten, gaan de kosten voor deze dingen flnk omlaag als de schaal vergroot wordt, simpelweg omdat dingen goedkoper ingekocht kunnen worden.

### S3 gratis service:
Simple Storage Service.  

Bij het inschrijven krijgen nieuwe AWS klanten 5GB van Amazon S3 storage in de standaard S3 storage class; 20.000 GET requests; 2000 PUT, COPY, POST of LIST Requests; en 100GB aan Data Tansfer per maand gratis voor het eerste jaar.

### EC2 gratis service:
750u/maand aan compute. Om in de gratis tier te blijven, gebruik alleen *Micro Instances*.

### Services die altijd gratis zijn:
[Overzicht:](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=tier%23always-free&awsf.Free%20Tier%20Categories=*all)

### capex:
*Capital Expenditure*.  
Geld dat je uitgeeft om je server(park) aan te schaffen en te onderhouden. Dit gaat niet alleen om de  hardware die nodig is, maar ook om de mensen die je moet inhuren om het te onderhouden, de stroomkosten, de ruimte die het inneemt etc.

### opex:
*Operational Expenditure*.  
De kosten van het uitbesteden van alle fysieke, servergerelateerde naar de cloud.


## Opdracht
### Bestudeer:
- De vier voordelen van het AWS picing model.
- AWS free teer voor: 
	- S3
	- EC2
	- Services die altijd gratis zijn
- Begrijp de verschillen tussen capex en opex

### Opdracht:
- Maak een alert aan die je kan gebruiken om jouw cloud kosten in de gaten te houden.
- Snap de opties die AWS aanbied om inzicht te geven in de kosten.

### Gebruikte bronnen
[3 Voordelen:](https://aws.amazon.com/pricing/?aws-products-pricing.sort-by=item.additionalFields.productNameLowercase&aws-products-pricing.sort-order=asc&awsf.Free%20Tier%20Type=*all&awsf.tech-category=*all)
[4e voordeel:](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html)  
[4 voordelen:](https://dzone.com/articles/the-cost-of-the-cloud-the-ultimate-aws-pricing-gui)  
[capex/opex](https://www.youtube.com/watch?v=Nrby-PZWxU4)  

### Ervaren problemen
Zeker bij het kosten onderdeel moet ik mijn interne accountant wakker schudden om het goed te begrijpen. Dit is een vaardigheid die ik nog moet ontwikkelen, maar ik zie wel in, mede door het te bespreken in het team, dat dit, ook als Cloud Engineer een waardevolle vaardigheid is om te beheersen.

### Resultaat
Ik heb mijn oude, al bestaande budget ($0), aangepast naar $100, met een alert als ik over de $95 heen ga. Deze wordt per e-mail naar mij verstuurd.  
Ik heb dit gedaan door in de zoekbalk **Budgets** in te typen en de link te volgen.
Screenshot staat in de 00_includes folder als [AWS-02.png](/00_includes/AWS-02.png).  

![](/00_includes/AWS-02.png)

Opties die AWS aanbiedt om inzicht te krijgen in de kosten:  
AWS heeft een hele portal die meerder opties heeft om inzicht te krijgen in de kosten en eventueel geld te besparen. Om hier te komen hoef je in de search bar alleen maar "Cost explorer" in te typen en de link naar de portal verschijnt automatisch. Screenshot staat als [AWS-02-2.png](/00includes/AWS-02-2.png) in de 00_includes folder.  
![](/00_inlcudes/AWS-02-2.png)  
