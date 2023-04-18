# IP-adressen
Wat zijn IP-adressen, en hoe werkt dat op mijn netwerk?

## Key-terms

### IP-adres:  
Een IP-adres kan je zien als een adres en huisnummer voor je apparaat. Zonder dit kan je apparaat niet worden gevonden op een netwerk.

### IPv4:  
Deze versie van IP-adressen wordt nog het meest gebruikt, ondanks dat ze in feite 'op' zijn.
De notatie is in decimale getallen in 4 blokken van 3 getallen in de *Dotted Decimal Notation*.   Aangezien het 32-bit is, zijn er maar 2<sup>32</sup> = 4,294,967,296 IP-adressen mogelijk, waarvan er bijna 600 miljoen zijn gereserveerd, waardoor er grofweg zo'n 3.7 miljard adressen mogelijk zijn voor openbaar gebruik. Dit is zeker sinds de opkomst van Smartphones het  *Internet of Things*, IoT, een groot probleem aan het worden. Om saturatie te voorkomen, is onder andere NAT en IPv6 ontwikkeld.

### IPv6:
De oplossing voor het probleem van het opraken van IPv4 adressen. De hoeveelheid mogelijke combinaties is zó groot, dan één persoon miljarden adressen kan gebruiken.
IPv6 wordt genoteerd in hexadecimaal

### Public en Private IPs:
Een *Public IP* is een IP-adres dat in een WAN wordt gebruikt en een *Private IP* is een adres dat binnen een LAN wordt gebruikt. *Public IPs* mogen maar één maal voorkomen, terwijl een *Private IP* maar één maal per LAN gebruikt kan worden. Er zijn bepaalde IP-adressen gereserveerd voor gebruik op een LAN, deze komen niet voor als *Public IP*.
Een *Public IP* krijg je van je ISP, en een *Private IP* kan je op je apparaat zelf instellen, of wordt aangewezen door jouw router.

### Statisch IP adres:
Een statisch IP adres is een instelling die je kan doen op het apparaat zelf of op sommige routers, dat er voor zorgt dat dit apparaat een vast IPv4 adres krijgt op dat netwerk. Als het op de router wordt ingesteld, dan wordt dit adres gereserveerd voor het bedoelde apparaat. Als het op het apparaat is ingesteld, dan vraagt het dit adres aan bij het verbinden met het netwerk. Mocht dit adres al in gebruik zijn of gereserveerd, dan weigert de router de verbinding tot er een ander adres wordt aangevraagd.

### Dynamisch IP adres:  
Een Dynamisch IP adres is een IP adres dat niet aan een bepaald apparaat is gekoppeld. Iedere keer dat het apparaat verbinding maakt met het zelfde netwerk, krijgt deze een willekeurig IP adres dat binnen dat netwerk valt toegewezen.

### NAT:
Dit staat voor *Network Address Translation*. Dit is één van de antwoorden op IPv4 exhaustion door het, met gebruik van *Private IPs*, mogelijk te maken om op veschillende LANs dezelfde IPv4-adressen te gebruiken. Dankzij NAT kunnen we nu nog IPv4 gebruiken, anders waren we al lang door alle adressen heen.
In het kort vertaalt dit een *Private IP* naar een *Public IP* en vice versa. Dit maakt het überhaupt mogelijk om *Private IPs* te gebruiken.
Voor IPv6 is NAT niet meer nodig, omdat het onderscheid tussen een *Private- en Public IP* niet meer nodig is gezien de enorm grote hoeveelheid mogelijke IPv6 adressen.

## Opdracht
-   Ontdek wat je publieke IP adres is van je laptop en mobiel op wifi.
    
-   Zijn de adressen hetzelfde of niet? Leg uit waarom.
    
-   Ontdek wat je privé IP adres is van je laptop en mobiel op wifi.
    
-   Zijn de adressen hetzelfde of niet? Leg uit waarom.
    
-   Verander het privé IP adres van je mobiel naar dat van je laptop. Wat gebeurt er dan?
    
-   Probeer het privé IP adres van je mobiel te veranderen naar een adres buiten je netwerk. Wat gebeurt er dan?

### Gebruikte bronnen
Official Cert Guide CCNA 200-301 Volume 1 - Wendell Odom

### Ervaren problemen
De problemen bij deze opdracht waren deels dezelfde problemen die ik in de eerdere opdrachten ben tegengekomen; diepgang. Aangezien in voor mijn planning iets achterloop, kan ik niet héél lang stoppen in de materie.
Het tweede punt waar ik tegenaan liep was het OS van mijn telefoon dat zeer privacy gericht is, dus dingen blokkeerd, zoals het instellen van een statisch IP adres.. Gelukkig heb ik in het verleden genoeg gerotzooid met mijn netwerk en IP instellingen dat ik weet wat er zal gebeuren.

### Resultaat
**Antwoorden op vragen:**
- Het publieke IP adres van mijn laptop en mobiel zijn verschillend, omdat ik achter een VPN zit en beide apparaten verbinding maken met een andere server. Uit veiligheidsoverweging plaats ik dit adres niet hier.
- Zie boven.
- Het privé IP adres van mijn laptop is 192.168.2.6, en die van mijn mobiel is 192.168.2.3. Deze heb ik statisch gehouden en mijn router geeft deze adressen uit.
- Uiteraard zijn deze adressen niet hetzelfde, om een IP-conflict te voorkomen.
- Om een of andere reden blijven beide apparaten online en verbonden met het netwerk. De router geeft ook gewoon aan dat er 2 devices zijn met hetzelfde IP adres. Mobile data was uitgezet, en ook de VPN stond uit. (afbeelding in 00_includes folder als [NTW-05.png](/00_includes/NTW-05.png)).  

![](/00_includes/NTW-05.png)

- Wanneer het IP adres van mijn mobiel veranderd wordt naar een IP adres buiten mijn netwerk, dan is het zijn eigen netwerk en kan het geen verbinding maken de rest van het netwerk, inclusief het internet. De router ziet het apparaat niet eens.
