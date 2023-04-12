# OSI en TCP/IP
In deze opdracht gaan we kijken naar het OSI- en TCP/IP netwerk model.

## Key-terms

### Wat is een networking model?
Een *networking model*, ookwel *networking architecture* of *networking blueprint* genoemd, bestaat uit een uitgebreide set documenten. Elk individueel document bescrijft een kleine, noodzakelijke functie voor het netwerk. De documenten samen definiëren alles dat nodig is voor het functioneren van het netwerk. Sommige documenten definiëren een *protocol*, andere documenten definiëren fysieke noodzakelijkheden, zoals bijvoorbeeld de voltages van de kabeltjes voor het verzenden van data.

Een networking model is vergelijkbaar met een blauwdruk voor het maken van een huis; er staat in waar alles moet zitten en welke materialen er nodig zijn. Er staat alles in wat een huis degelijk zou moeten maken.

### Geschiedenis:
Tegenwoordig gebruikt, op wellicht een enkel netwerk na, elk netwerk het netwerk model van TCP/IP.
In den beginne waren er uiteraard nog geen netwerkprotocollen, dus moesten deze nog worden gemaakt. De eerste protocollen waren vendor-specifiek. Zo had IBM bijvoorbeeld het Systems Network Architechture (SNA) in 1974. Andere bedrijven hadden hun eigen modellen. Deze modellen/protocollen waren alleen te gebruken in netwerken met apparatuur van de zelfde bedrijven. Via complexe methodes was het mogelijk om deze netwerken te koppelen.
Deze modellen functioneerde an sich prima, maar omdat er geen standaard was, was het het Wilde Westen. De wens naar een non vendor-specifieke oplossing was groot onder de gebruikers.

De International Organisation of Standardization (ISO) nam het eind jaren '70 op zich om zo'n model te ontwerpen. Dit resulteerde in het OSI (Open Systems Interconnection) model. 
Een andere organisatie die een open model ging ontwerpen was de U.S. Department of Defence (DoD). Meerdere universiteiten werkten mee aan het ontwikkelen van dit model. Dit resulteerde in TCP/IP.

In de jaren '90 werden voor een korte periode zowel OSI als TCP/IP gebruikt in apparaten. Aan het eind van de jaren '90 was TCP/IP de winnaar van de twee. Er waren ook nog veel vendor-specifieke modellen in gebruik.

Tegenwoordig is TCP/IP het dominante model.

Ondanks dat het OSI model het niet heeft gered, wordt de terminologie er achter wél nog heel veel gebruikt.

### OSI Model:
Het OSI model is een *Networking model* dat tegenwoordig niet meer gebruikt wordt in computernetwerken. Het is 'verslagen' door TCP/IP. Het model wordt nog wel veel aangehaald in de support wereld, omdat het prachtig uiteen zet op welke volgorde je het makkelijkst kan troubleshooten.
Het OSI model ziet er als volgt uit:

|Layer # |Naam |
|--- |----|
|7 |APPLICATION|
|6 |PRESENTATION|
|5|SESSION|
|4 |TRANSPORT|
|3 |NETWORK|
|2 |DATA LINK|
|1 |PHYSICAL|

Voorbeeld van protocollen die per laag worden gebruikt:

Layer | Voorbeeld Protocollen
---| ----
Application | HTTP, POP3,SMTP
Presentation | TLS, SSL
Session | PPTP, NetBIOS
Transport | TCP,UDP
Internet | IP,ICMP
Data Link & Physical | Ethernet, 802.11


### TCP/IP Model:

TCP/IP refereert naar en definiëert een groot aantal protocollen. Om een protocol te definiëren wordt gebruik gemaakt van documenten die *Requests For Comments* (RFC) heten. Het zou zonde zijn om al bestaande protocollen opnieuw te definiëren, dus wordt er verwezen naar de protocollen. Je hoeft het wiel niet opnieuw uit te vinden.
Een mooi voorbeeld zijn de protocollen van de Ethernet LAN, die al door het *Institute of Electrical and Electronic Engineers* (IEEE) zijn gedefineerd.

Om het model beter te begrijpen zijn een aantal functies onderverdeeld in categoriën, *layers* genaamd.
Er zijn verschillende versies van het model in omloop, een versie met 4 lagen, maar ook een 5 lagen versie met andere namen voor de lagen als hier onder gebruikt. De versie die hier onder staat is de meest recente en sluit ook beter aan bij het OSI model.


Het TCP/IP model ziet er als volgt uit:  

|Layer # |TCP/IP Model |
|--- |---- |
|5-7 |APPLICATION |
|4 |TRANSPORT |
|3 |NETWORK |
|2 |DATA LINK |
|1 |PHYSICAL |

Voorbeeld van protocollen die per laag worden gebruikt:

Layer | Voorbeeld Protocollen
---| ----
Application | HTTP, POP3,SMTP
Transport | TCP,UDP
Internet | IP,ICMP
Data Link & Physical | Ethernet, 802.11


### Functie van de layers:

#### Layer 1, Physical:
Deze layer is verantwoordelijk voor de protocollen die op hardwareniveau functioneren. Het gaat hier om voltages, kabeltypes, de WiFi protocollen, etc.

#### Layer 2, Data-Link:
Deze layer vertaalt de data verkregen van layer 1 naar een *frame*. Ook worden de MAC-adressen van de hosts gebruikt om de fysieke locatie ervan te vinden op het netwerk.

#### Layer 3, Network:
Deze layer koppelt het MAC-adres verkregen van layer 2 aan een IP-adres. Hierin staat onder andere wie de verzender is en wie de ontvanger moet zijn. De network layer is te vergelijken met de post- en pakketdienst. Iemand verstuurt een brief, en het is aan de network layer om deze te bezorgen.

#### Layer 4, Transport Layer
Deze layer ze de ontvangen data van layer 5 om in *packets*, kleine stukjes data die makkelijker verzonden kunnen worden. Dit is ook de layer waar de error checking gedaan wordt.

#### Layer 5, Session
Deze layer creëert en beindigt *sessions*.

#### Layer 6, Presentation
Deze layer doet de encryptie en decryptie van de data. Het zorgt er voor dat de data in een leesbaar format staat voor de Application layer.

#### Layer 7, Application
De Application Layer definiëert niet de software zelf, maar wel de protocollen die de software gebruiken, zoals HTTP bij Browsers. Een interface tussen software en netwerk. De software is te ondescheiden, omdat het gebruik maakt van *ports*, zoals port 80 bij HTTP.

## Opdracht
Bestudeer:
- Het OSI model en de toepassing
- Het TCP/IP model en de toepassing

### Gebruikte bronnen
Official Cert Guide CCNA 200-301 - Wendell Odom

### Ervaren problemen
Het grootste probleem waar ik tegenaan liep was dat ik, omdat ik begonnen was een een zelfstudie CCNA, al een redelijke kennis heb van de materie en niet goed wist hoe diep ik in deze materie moest duiken voor deze opdracht. Bij navraag bij de LC werd aangegeven dat het niet heel erg diep hoefde, maar als ik tijd over had dat ik zo diep mocht gaan als ik wilde.

### Resultaat
Dit document.
