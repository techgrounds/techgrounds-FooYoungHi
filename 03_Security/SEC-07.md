# Passwords
Het leren begrijpen van het nut van veilige wachtwoorden en manieren om ze veilig op te slaan.

## Key-terms

### Hashing:
Via een formule iets omzetten in een code.
Hashing is *géén* encryptie. Wanneer de hash is aangemaakt, is het niet te 'ontcijferen'. Dit is het grote verschil met encryptie.
Er hoeft dus, in tegenstelling tot symmetric encryption, geen key ergens worden opgeslagen die gecompromitteerd kan worden.

### Rainbow Table:
Een rainbow table is een tabel waar bekende hashes instaan met corresponderende wachtwoorden. Deze zijn zelf te maken met eigen input, of online te vinden waar de meest voorkomende wachtwoorden in staan.

### Salt:
Een willekeurig gegenereerde code, verschillend tussen 6- en 96-bits.
Een manier om elke password hash uniek te maken. Tijdens het omzetten van het password in een hash, wordt eerst een *salt* gegenereerd en deze wordt voor het plain-text password gezet. Daarna wordt deze in zijn geheel encypt, waardoor de hash, ook bij 2 gelijke wachtwoorden altijd uniek is.

## Opdracht
- Zoek uit was *hashing* is en waarom het beter is dan *symmetric encryption* om passwords op te slaan.
- Zoek uit hoe een *rainbow table* gebruikt kan worden om gehashete passwords te kraken.
- Hier onder staan 2 md5 password hashes. 1 is een zwak wachtwoord, de ander is 16 willekeurig gegenereerde karakters. Probleer beide op te zoeken in een rainbow table. `03F6D7D1D9AAE7160C05F71CE485AD31`
`03D086C9B98F90D628F2D1BD84CFA6CA`
- Maak een nieuwe user aan in je VM met password 12345. Zoek de hash  Vergelijk de hash met een peer.

### Gebruikte bronnen
[Crackstation](https://crackstation.net/)
[Linux hash](https://www.cyberciti.biz/faq/understanding-etcshadow-file/)

### Ervaren problemen
Geen.

### Resultaat
Het invoeren van de hashes in de rainbowtable van Crackstation.net gaf het volgende resultaat:
03F6D7D1D9AAE7160C05F71CE485AD31 = welldone!
03D086C9B98F90D628F2D1BD84CFA6CA = *Not found*
De 2e has is staat niet in de table van bekende hashes, dus is het als wachtwoord al veiliger.

Ik heb een nieuwe user aangemaakt in mijn Linux VM met het password 12345.
De *salt* hiervan is `ZtnEpS7RmSk5B5hy` en de *hash* is `Y1gifAqOM3bdMaZbwVLRKOj0baux0V2Ap5Hfs3BuW85mWKolUT1xY99IGb8WlPkvjb6ciRxN9uocwrWbdyMDt`.
De hash van een peer is anders, omdat deze gemaakt wordt samen met de *salt*. Aangezien de *salt* random is gegenereerd, is de hash ook voor hetzelfde password steeds anders.
