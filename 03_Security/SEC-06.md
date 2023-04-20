# Public key infrastructure
Bekijken wat de functie is van een versleutelde website en hoe het werkt.

## Key-terms

### X.509:
Dit is een standaard format voor *public key certificates*. De belangrijkste functie is het verlenen van toegang tot de *public key* voor een specifieke host. Het bevestigt ook dat de *public key* hoort bij de persoon in kwestie.  

### Public key infrastructure (PKI):
Dit is de *infrastructuur* die er voor zorgt dat wanneer iemand met een ander wilt communiceren, deze zeker weet dat de public key die ze krijgen ook daadwerkelijk van de bedoelde ontvanger is.  
Dit is het pad naar het verkrijgen van een *signed certificate* van een *Trusted Third Party, TTA*. De TTA is in dit geval de *Certification Authority*.
Je apparaat verstuurd een *Certification Request (CR)* naar deze *CA*. Bij deze *CA* laat je wat gegevens over jezelf achter, waar derden aan kunnen zien dat het certificaat bij jou hoort. Wanneer de CA het *signed certificate* afgeeft, is deze samen met je *public key*, door iedereen te raadplegen, zodat jouw 'identiteit' geverifieerd is voordat de communicatie tot stand komt.

### Certification Authority (CA):
Een *Certification Authority, CA* kan in een digitaal ondertekend bestand aangeven van wie de public key is. Hierdoor kan iedereen die de *public key* ontvangt er zeker van zijn dat de key is van wie ze denken dat hij is, zodat de versleutelde berichten aankomen bij de bedoelde bestemming.  
Essentieel hierbij is de betrouwbaarheid van de *CA*.

## Opdracht
- Maak een *self-signed certificate* voor je VM.
- Analyseer een aantal *certification paths* van een aantal websites.
- Vind een lijst van *trusted certificate roots* op je systeem. Bonuspunten als je dit ook op je VM kan vinden.

### Gebruikte bronnen
[X.509](https://www.youtube.com/watch?v=FrYLdfYj1co&pp=ygUPeC41MDkgZXhwbGFpbmVk)
[Self-signed certificate](https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-20-04)

### Ervaren problemen
Ik ben een flinke tijd bezig geweest om te proberen om de SSL werkende te krijgen op de site zelf. Ik ben tot de conlcusie gekomen dat het niet kán werken, omdat port 443 niet geforward is naar onze VMs.

### Resultaat
De *self-signed certificate* is aangemaakt met de code:
`sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/test.key -out /etc/ssl/certs/test.crt`

Voor zover ik het heb kunnen vinden staan de *trusted certificate roots* in Linux in `/usr/share/pki/ca-trust-source/`
