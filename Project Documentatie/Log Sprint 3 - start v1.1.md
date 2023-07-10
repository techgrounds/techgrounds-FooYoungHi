## Log Maandag 03 Juli 2023:

### Dagverslag:
Vandaag hoofdzakelijk de nieuwe eisen van het project geimplementeerd in de planning en het design. Daarnaast veel administratie gedaan om alles weer netjes te hebben.

### Obstakels:
Het grootste obstakel van vandaag was de slechte staat van mijn administratie.

### Oplossingen:
De enige oplossing voor de slechte administratie was de tijd pakken om dit goed te doen.

### Learnings:
Administratie goed bijhouden is essentiëel voor het overzicht.

---
## Log Dinsdag 04 Juli 2023:

### Dagverslag:
Vandaag de hele dag bezig geweest met ALB. Geprobeerd ook al eisen van v1.1 te implementeren.


### Obstakels:
Het deployen van de code gaat steeds fout. Ik krijg een error dat de listener port al bestaat en niet weer kan worden toegevoegd. Hoe ik dit kan aanpakken moet ik nog uitzoeken.

### Oplossingen:
Ik ben nog op zoek naar een oplossing door in de documentatie te kijken en error codes op te zoeken.

### Learnings:
ChatGPT is zeer onbetrouwbaar als het gaat om code en feitelijke kennis. Het verstandigst is om de officiële documentatie te gebruiken.

---
## Log woensdag 05 Juli 2023:

### Dagverslag:
Vandaag de hele dag bezig geweest met de ALB, net als gisteren. Het obstakel van gisteren is overwonnen.

### Obstakels:
De health check van de webserver via de TargetGroup blijft maar unhealthy, ondanks dat het prima te benaderen is via het internet.

### Oplossingen:
Ik ben er via stackoverflow achter gekomen dat ik niet moest aangeven dat hij moest kijken in /var/www/html/healthcheck.php, maar gewoon in /healthcheck.php. Na dit gedaan te hebben werkt het.

### Learnings:


---
## Log donderdag 06 Juli 2023:

### Dagverslag:
Vandaag wederom bezig geweest met de ALB en ASG. De autoscaling is intussen werkend gekeregen

### Obstakels:
Ik wilde het scalen mooier maken dan noodzakelijk was. Er ging teveel tijd in zitten, terwijl ik een werkende oplossing had dat goed genoeg was voor de MVP.

### Oplossingen:
In overleg met PO Casper besloten dat als het werkt, ik het kan gebruiken. Ik heb mijn code weer aangepast naar de werkende versie.

### Learnings:
Houd de MVP in je achterhoofd. Werkende code is de eis. Geen schoonheidsprijs nodig.

---
## Log vrijdag 07 Juli 2023:

### Dagverslag:
Vandaag bezig geweest met het SSL certificaat werkende krijgen. Ik heb een certificaat aangemaakt op mijn eigen domein, zodat ik geen self-signed certificate hoef aan te maken, wat werk scheelt.

### Obstakels:
Helaas kon ik niet verder met het certificaat, omdat het even lijkt te duren voordat de DNS records zijn geupdate.

### Oplossingen:
Er zit niets anders op dat om tot maandag te wachten.

---

## Einde Sprint.
Op het werkende krijgen van het certificaat na is de sprint van deze week gehaald.