# Firewalls
Werken met de ufw (Uncomplicated Firewall) in Ubuntu.

## Key-terms

### netfilter:
Dit is een *packet filtering* system dat in de linux kernel zit. De manier om dit te bewerken gaat via *ip tables* commands. *Ip tables* is een zeer complete firewall die goed te configureren is en flexibel in te zetten is.  
Direct werken met netfilter is mogelijk, maar behoorlijk complex en heeft een flinke leercurve. Hierdoor zijn er een aantal frontend applicaties ontwikkeld die veel van het werk van je overnemen.


### ufw:
*Uncomplicated firewall*, een frontend voor *iptables*.
Via ufw bewerk je de *ip tables* op een eenvoudige, beginner vriendelijke manier.
Ondanks de eenvoudige opzet, is er ook de mogelijkheid om dingen te finetunen.

### stateful/stateless:
Een **stateless firewall** inspecteert waar de packet naar toe gaat en vandaan komt, met nog wat andere parameters om te kijken of het een bedreiging is. Deze parameters moet van te voren worden ingevoerd door de admin. Als de packet buiten de geaccepteerde parameters valt, wordt deze tegen gehouden.

Een **stateful firewall** gaat de inhoud van de packets inspecteren. Het gedrag van de packets wordt in de gaten gehouden, en als er iets verdachts voordoet, dan wordt de data tegengehouden. Doordat het gedrag van de packets in de gaten wordt gehouden, kan er ook naar patronen worden gekeken.  
Ook verdacht gedrag dat *niet* door de admin is ingesteld kan worden tegengehouden.

##### Voor- en nadelen van een *stateful firewall*:
**voordelen:**
- Ze kunnen kwaaraardige data detecteren die probeert je netwerk binnen te dringen.
- Ze hebben niet veel open poorten nodig voor goede communicatie.
- Het kan leren van verdacht gedrag van packets en dit in de toekomst deze patronen herkennen en weer toepassen in andere situaties. Op deze manier kunnen aanvallen sneller en efficiënter worden tegengehouden zonder dat deze informatie via een update hoeft te worden toegevoegd. Dit is het grootste voordeel van een **stateful firewall**.  

**Nadelen**
- Sommige firewalls kunnen voor de gek worden gehouden door de data, waardoor het toch het netwerk op komt.
- Ze zijn gevoeliger voor *Man in the middle, MITM* aanvallen.

##### Wanneer stateful of stateless?
Voor een individuele gebruiker is over het algemeen een *stateless* oplossing prima, aangezien de kans op gerichte cyberaanvallen niet heel erg groot is. *stateful* firewalls zijn over het algemeen ook duurder. Daarnaast heeft een *stateful* firewall de nodige kennis en vaardigheden nodig om goed te kunnen gebruiken.

Voor een klein bedrijf geldt hetzelfde. De kosten/baten van een *stateful* firewall komen vaak niet bij elkaar in de buurt.

Voor de enterprise bedrijven is het wél een goed idee, omdat ze simpelweg een interessanter doelwit zijn voor aanvallen. 

### Hardware- & software firewall:

Het meest vanzelfsprekende verschil tussen een hardware en software firewall is dat de een een fysieke kast is, en de ander een programma dat op je apparaat draait. In essentie doen ze hetzelfde, maar de manier waarop ze dat doen verschilt.

#### Voor- en nadelen van een software firewall:
- De aanschafkosten zijn vrij laag. Veel software firewalls hebben echter maandelijkse of jaarlijkse kosten om het up-to-date te houden, wat op den duur véél meer kost dan een hardware oplossing.
- Het neemt geen fysieke ruimte in, omdat het software is.
- Makkelijk om te installeren en aan het werk te zetten.
- Ze moeten op *alle* apparaten op het netwerk worden geïnstalleerd en worden geupdate, wat nog wel eens fout kan gaan.
- Ze nemen wat resources in op de host computers.
- Ze kunnen per host de uitgaande data tegenhouden, wat voorkomt dat 1 gecompromitteerde host een heel netwerk kan aantasten.

#### Voor- en nadelen van een hardware firewall:
- Aangezien de firewall direct achter de router zit, hoef je niet op elk apparaat een firewall te installeren.
- Er zit vaak meteen antivirus software in.
- Het gebruikt geen resources van de individuele PCs
- Het is véél beter te configureren
- Als er toch iets doorheen glipt, kan de gecompromitteerde host het hele netwerk aantasten. Dit is enigszins te beperken door op meerdere plekken een firewall bijvoorbeeld tussen switches te plaatsen die de outgoing traffic in de gaten houden.
 
## Opdracht
-   Installeer een webserver op je VM.
-   Bekijk de standaardpagina die met de webserver geïnstalleerd is.
-   Stel de firewall zo in dat je webverkeer blokkeert, maar wel ssh-verkeer toelaat.
-   Controleer of de firewall zijn werk doet.

### Gebruikte bronnen
[ufw definitie:](https://wiki.ubuntu.com/UncomplicatedFirewall)  
[Stateful/Stateless](https://www.fortinet.com/resources/cyberglossary/stateful-vs-stateless-firewall)
[Hardware en software firewall](https://www.fortinet.com/resources/cyberglossary/hardware-firewalls-better-than-software)

### Ervaren problemen
Ik dacht dat ik Apache2 nog had geinstalleerd en wilde even snel de poorten toelaten tot de firewall. Toen er niets gebeurde toch maar even gaan kijken naar de status van Apache en die bleek dus niet geïnstalleerd. Nadat ik dit had gedaan ging de opdracht vrij simpel.

### Resultaat
De standaardpagina van Apache2 is zichtbaar als ik `sudo ufw allow 'Apache Full'` invoer, en niet zichtbaar (connection timed out), wanneer ik `sudo ufw deny 'Apache Full'` invoer.  
De reden dat ik 'Apache Full' heb gebruikt en niet 'Apache', is dat ik nu ook de https port 443 heb toegevoegd.
SSH is ten alle tijde bereikbaar geweest.
