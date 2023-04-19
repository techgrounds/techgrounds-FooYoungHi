# Symmetric Encryption
Uitleg van symmetric encryption en de geschiedenis van encryptie.

## Key-terms

### Encryption:
Encryptie, oftewel het versleutelen van data. Het versleutelen van data gebeurt met een *key*. Deze *key* is een unieke combinatie van nummers, getallen etc.

### Symmetric Encryption:
Met deze encryptiemethde wordt gebruik gemaakt van 1 *key*. Deze key moet worden gedeeld met de ontvanger om de berichten te kunnen versleutelen. Het grote nadeel van deze methode is dat de *key* zelf niet versleuteld is. Het is dus vrij gemakkelijk om, wanneer je deze key onderschept, de communicatie van de twee partijen te kunnen lezen.

### Cipher:
De naam van de 'sleutel' om de encryptie mee te ontcijferen.
Een hele bekende en notoire cipher was de Lorenz cipher uit WO2.
Digitale cyphers die we op dit moment gebruiken is AES en MD5.

## Opdracht
- Zoek een andere historische *cipher* naast de *Caesar cipher*.
- Zoek 2 digitale ciphers die nu worden gebruikt.
- Stuur en symmetric encrypted bericht naar iemand op het openbare slack kanaal, samen met de key. Het openbare kanaal is de *enige* manier waarop beide verzonden mogen worden.
- Bekijk de tekorten van symmetric encryption.

### Gebruikte bronnen
[Encryptie website:](https://www.devglan.com/online-tools/aes-encryption-decryption)
[Lorenz cipher](https://www.youtube.com/watch?v=RCWgOaDOzpY&pp=ygUNbG9yZW56IGNpcGhlcg%3D%3D)  

### Ervaren problemen
Voor mijn eerste encryptie idee werkte slack tegen, omdat deze alle metadata uit een bestand haalt.

### Resultaat

**Encrypte zin:**
Ik heb hard zitten denken hoe ik de key zo lastig mogelijk te vinden kon maken. Het eerste idee dat ik had was om het logo van het bedrijf Meta te nemen, met als ALT text 'Data'. Dit samen zou MetaData vormen, wat aangeeft dat de key in de metadata van de afbeelding verstopt zou zitten. Helaas lukte dit niet, omdat Slack de metadata van afbeeldingen weghaalt voor privacy redenen. Een omweg verzinnen ging me te ver. Zeker omdat ik nog een tweede idee had, wat net zo lastig was.
Het tweede idee was om een plaatje van Princess Peach te gebruiken waar de text "Hurry up and save me" in stond. De ALT text was "Luister naar de prinses!" Ik had de 'filename' in slack veranderd in PrincessPeach.jpg om de ware filename te verbergen en medecursisten te misleiden. Het idee was dat je de image ging downloaden (Saven!) en zo zou je de echte filename vinden, BowserMoetHuilen.jpg. Met deze zin (zonder .jpg) kan je het decrypten tot "De prinses in gered!"
Uiteraard werd deze wel gekraakt, aangezien de key in plain text is.
