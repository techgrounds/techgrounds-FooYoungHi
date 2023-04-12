# Introductie tot netwerk apparaten
In deze oefening gaan we kijken naar de functie van de meest voorkomende netwerkapparaten en kijken hoe mijn router de verbonden apparaten aangeeft.

## Key-terms
**Repeater**: 
Een repeater is een 'dom' apparaat. Het werkt op layer 1. Het enige dat het doet is het binnenkomende signaal doorgeven en 'versterken'. Dit zorgt er voor dat kabels of een WiFi signaal verder kan komen dan normaal.

**WAP:**
Wireless access point (WAP). Dit apparaat zorgt er voor dat je draadloze apparaten via WiFi verbinding kunnen maken met de rest van het netwerk. Naast deze layer 1 functie, heeft het vergelijkebare functies als een Switch, maar dan voor draadloze apparaten.

**Switch**:
Een switch is een apparaat wat er voor zorgt dat apparaten op een LAN met elkaar kunnen communiceren.
Het is een  layer 2 apparaat wat er voor zorgt dat de packets op het LAN terecht komen op de juiste PC. Een switch heeft in een *MAC-address table* de fysieke poort gekoppeld aan het *MAC-adres* van de host. Deze table wordt om de zoveel tijd ververst, zodat het up to date is.
Een switch 'kent' een host bij zijn *MAC-adres*, niet aan het *IP-adres*

Veel managed switches hebben ook beperkte layer3 functionaliteit. Deze heten een *multilayer switch*. Deze kunnen ze bijvoorbeeld ook IP-adressen uitgeven, wat meer de taak is van de router. Deze switches zijn ontworpen voor een *intranet*, dus de meesten hebben geen WAN-poort. Een van de doelen is om het routen van *packets* tussen *VLANs* (virtual LANs) te faciliteren.
Ook zijn er nog layer 4 switches, die zich ook nog bezig houden met TCP en UDP poorten.

**Router:**
Een router is de verbinding tussen verschillende LANs en een verbinding met een WAN. Voor de gemiddelde persoon is een router de toegang tot het internet, maar dat is niet de enige functie. Via een router kan je ook verbinding maken met een andere LAN.
Een router is een layer3 apparaat, het maakt gebuik van *routing tables*

De router die de meeste mensen voor thuisgebruik of *SOHO* (Small Office, Home Office) van hun ISP krijgen is een multifunctioneel apparaat; het is een *modem*, *router* en *swich* in 1. Deze levert functionaliteit in voor gebruiksgemak. Voor de meeste klanten zijn deze apparaten prima, maar als je meer wilt met je netwerk loop je al snel tegen grenzen aan. Zeker omdat sommige ISPs de functionaliteit van het apparaat sterk begrenzen, voor meer gebruiksgemak, maar ook om te voorkomen dat een leek er  dingen in gaat veranderen, wat weer voor extra support vragen kan zorgen.

## Opdracht
- Benoem en beschrijf de functies van veel voorkomend netwerkapparatuur
- De meeste routers hebben een overzicht van alle verbonden apparaten, vind deze lijst. Welke andere informatie heeft de router over aangesloten apparatuur?
- Waar staat je DHCP server op jouw netwerk? Wat zijn de configuraties hiervan?

### Gebruikte bronnen
Official Cert Guide CCNA 200-301 Volume 1 - Wendell Odom

### Ervaren problemen
Het grootste probleem waar ik tegenaan liep was hoe diep ik in de stof ging duiken. Ik ben in het verleden aan een zelfstudie begonnen voor de CCNA, waardoor mijn kennis en begrip van netwerken naar alle waarschijnlijkheid boven deze opdracht uit steken. Deze kennis moet nog wel weer worden aangescherpt, maar ik heb besloten om dit stukje bij beetje te doen wanneer de cursus hier om vraagt.

### Resultaat
Screenshots staan in de 00_includes folder als [NTW-02-2.png](/00_includes/NTW-02.png) en [NTW-02-2.png](/00_includes/NTW-02-2.png)

![](/00_includes/NTW-02-1.png)

![](/00_includes/NTW-02-2.png)
