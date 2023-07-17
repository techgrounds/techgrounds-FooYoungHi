## Log maandag 10 Juli 2023

### Dagverslag:
Vandaag bezig geweest met het werkende krijgen van de omschakeling van HTTP naar HTTPS. In de ochtend het certificaat werkende gekregen.

### Obstakels:
Ik had het probleem dat na het overschakelen naar HTTPS de Health Checks van de instances niet meer wilde lukken, waardoor er constand instances werden aangemaakt en vervolgens weer geterminate.

### Oplossingen:
Na goed te hebben nagedacht over de architectuur en logica van wat ik wilde, en na een interactief rubber-ducky moment bij de Q&A met Casper, was bevestigd dat niet álles HTTPS kon zijn, omdat het certificaat op de LB stond, en niet op de instance. Na dit te hebben geïmplementeerd in mijn code werkte alles goed.

### Learnings:
De problemen zijn niet altijd de code, maar soms is het wat je er mee wil doen wat niet logisch is.

---
## Log dinsdag 11 Juli 2023

### Dagverslag:
Vandaag heb ik het voor elkaar gekregen om de verbinding tussen de MGMT server en Webserver tot stand te krijgen. De route tables zijn correct ingesteld en er is contact via SSH.

### Obstakels:
Ik liep vast bij het automatisch detecteren en toevoegen van het IP-adres van de gebruiker. 

### Oplossingen:
Bij navraag aan Product Owner Casper was dit niet een wenselijke functie, omdat de persoon die het deployed niet per se de admin is die het onderhoudt. Dit maakt het makkelijker, aangezien nu de IP handmatig ingevuld kan worden.

### Learnings:
Zonder het te beseffen had ik de aanname gemaakt dat dit noodzakelijk was. Vóórdat ik hier aan was begonnen had in aan de PO moeten vragen of dit wel wenselijk was. Dit had veel tijd gescheeld.

---
## Log woensdag 12 Juli 2023:

### Dagverslag:
Vandaag de hele dag bezig geweest om de SSH verbinding tot stand te krijgen tussen mijn PC naar de webserver, met de mgmt server als bastion.

### Obstakels:
Ik kreeg geen contact met de mgmt server via SSH.

### Oplossingen:
Bleek dat windows niet standaard een SSH *server* heeft geinstalleerd, alleen de client. Na wat userdata te hebben toegevoegd bij de launch van de windows image heb ik de verbinding kunnen maken zoals ik die wilde.

### Learnings:
Niet blind aannemen dat iets geïnstaleerd is, maar verifiëren.

---
## Log donderdag 13 Juli 2023

### Dagverslag:
Vandaag mij bezig gehouden met het opzetten van de Aurora database.

### Obstakels:
Mijn teamgenoten gebruikten geen Aurora, maar andere RDS, dus konden ze mij niet helpen met instellingen.

### Oplossingen:
Goed gekeken naar de API guide van AWS en het in combinatie met Cloud Whisperer op kunnen lossen.

### Learnings:
Ondanks dat de rest van het team voor een andere oplossing heeft gekozen, gewoon mijn instinct gevolgd en een oplossing gekozen die volgens mij het verstandigst is.

---
## Log vrijdag 14 Juli 2023

### Dagverslag:
Vandaag de hele dag bezig geweest met een oplossing zoeken om de database te kunnen benaderen door zowel de webserver als de management server.

### Obstakels:
Het maken van een 'userdata' scrips voor windows is een stuk lastiger dan bij linux, aangezien er een appstore ontbreekt.

### Oplossingen:
Voorlopig is een handmatige install het makkelijkst. Niet de mooiste oplossing, maar het werkt.

### Learnings:
Soms is de MVP het maximaal haalbare.

---

## Einde Sprint
Op een paar kleine dingen na is het project klaar als MVP. Volgende sprint de puntjes op de i zetten.