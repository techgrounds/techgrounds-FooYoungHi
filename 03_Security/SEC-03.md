# Identity & Access Management
Authorisatie en Authenticatie.

## Key-terms

### Authorisation:
Hiermee wordt bedoeld welke toegangsprivileges je hebt. Dit kan gaan om of je wel of niet bepaalde programma's kan draaien, of je wel of niet toegang hebt tot bepaalde mappen op het netwerk etc.  
In Linux bijvoorbeeld, heeft een user geen authorisatie om bepaalde commands uit te voeren. Hiervoor is de root user nodig.

### Authentication:
Aangeven of je bent wie je zegt dat je bent.
"Wie ben je, en ben je het echt?"
Dit kan met bijvoorbeeld een wachtwoord on het internet zijn, maar op de luchthaven heb je bijvoorbeeld je paspoort nodig om je identiteit aan te tonen, waar ook weer je vingerafdruk in staat.
Om het online veiliger te maken wordt steeds vaker *MultiFactor Authentication* vereist.
Er zijn 3 types van authenticatie:  
- Iets dat je weet
- Iets wat je hebt
- Iets dat je bent

**Iets dat je weet**: Dit is bijvoorbeeld een wachtwoord of een pincode. Dit is door bijvoorbeeld phising te achterhalen.
**Iets wat je hebt:** Denk hierbij een een smartcard, een hardware key of een *One-time Password, OtP* code via bijvoorbeeld de google authenticator.
**Iets dat je bent:** Hiermee worden biometrische eigenschappen bedoeld, zoals je vingerafdruk, iris-scan, stem etc.

### MFA:
*MultiFactor Authentication*. Hiermee wordt bedoeld dat je meerdere manieren nodig hebt om ergens toegang tot te krijgen.  
Op dit moment wordt de *2-factor authentication, 2FA* het meest gebruikt.  
Zo heb je bijvoorbeeld bij DigID niet alleen een gebruikersnaam en wachtwoord nodig, maar moet je ook een code invullen die je per SMS krijgt toegestuurd.
Je hebt verschillende niveaus van veiligheid als het gaat om de MFA. Een SMS is bijzonder onveilig, omdat dit als *plain text* via de provider naar jouw mobiel gestuurd wordt, waardoor het door kwaadwillenden onderschept kan worden.  
Een veiliger alternatief is een *authenticator app* op de telefoon of tablet van bijvoorbeeld microsoft, google, of de opensource Aegis. 

### Principle Of Least privilege:
Dit is een *information security* dat inhoudt dat een user alleen de toegang heeft tot de specifieke data, resources en applicaties die nodig is voor het uitvoeren van de taak.  
Op deze manier kan je als bedrijf de kans op bijvoorbeeld malware significant verkleinen, omdat er veel minder mogelijkheiden zijn om binnen te komen.  
Het wordt vaak afgekort tot PoLP.  
Een mooi voorbeeld is een hotel: De gast heeft, naast toegang to de openbare ruimtes, alleen toegang tot de eigen kamer met behulp van een keycard. Een schoonmaker zal toegang hebben dat alle kamers, maar niet tot de technische ruimtes. Een persoon die het onderhoud doet, zal overal toegang tot hebben, omdat deze persoon overal bij moet komen.  
In de ideale wereld hebben ook de schoonmakers alleen toegang tot de kamers die ze die dag moeten schoonmaken, en de technische personen krijgen alleen toegang tot de ruimtes waar ze op dat moment moeten zijn.


## Opdracht

### Bestudeer:
- Het verschil tussen authenticatie en authorisatie.
- De 3 factoren van authenticatie en hoe MFA de veiligheid verbetert.
- Het principe van *least privilege* en hoe het veiligheid verbetert.

### Gebruikte bronnen
[Least privilege](https://www.youtube.com/watch?v=2rCgA3IbTg4)

### Ervaren problemen
Geen

### Resultaat
Zie *Key Terms*
