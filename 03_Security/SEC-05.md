# Asymetric Encryption
Experimenteren met Asymetric Encryption

## Key-terms

### Asymetric Encryption:
Waar je bij *symetric encryption* 1 key hebt om zowel te encrypten als decrypten,  heb je bij *asymetric encryption* 1 key voor het encrypten, en 1 om de decrypten. De *public key* en de *private key*. Zoals de namen eigenlijk al aangeven, is de *public key* de sleutel die publiek 'bekend' kan zijn, zodat verzenders een bericht kunnen versleutelen om naar jou te sturen. Met deze *public key* kan je alleen maar encrypten en *niet* decrypten, dus is het delen van deze sleutel veilig om te doen. De *private key* is alleen in handen van de ontvanger en met deze key is het versleutelde bericht te ontcijferen. Omdat deze key het apparaat van de ontvanger niet verlaat, is er geen risico dat deze onderschept wordt.

## Opdracht
- Genereer een key pair
- Stuur een asymetrisch encrypt bericht naar iemand in de openbare slack. Ze moeten dit bericht kunnen decrypten met hun key. De openbare slack is de enige manier om het bericht over te brengen.

### Gebruikte bronnen
[Key generator & En- en Decryption tool](https://www.devglan.com/online-tools/rsa-encryption-decryption)

### Ervaren problemen
Het was even kort nadenken hoe dit veilig gedaan kan worden. Al vrij snel was het logisch dat de *public* key gedeeld moest worden met de peers, en dat de peers met die key een bericht moesten encrypten om deze naar mij te sturen. Aangezien ik de *private key* heb, ben ik de enige die deze kan decrypten.

### Resultaat
Ik heb mijn *public key* gedeeld in het openbare slack kanaal, waarmee een aantal van mijn peers mij een versleuteld bericht hebben gestuurd. Met mijn *private key* kon ik deze ontcijferen.

Deze manier van versleutelen is veel veiliger dan de symetrische variant, omdat de key die ik openbaar maak alleen gebruikt kan worden om een bericht te versleutelen. Ik ben de enige met de sleutel om het bericht weer leesbaar te maken.

Public key:
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCC8hvdmpQGdQQXLKMwfkXbl+/UAfzqTzMC+NhY4dER0sYnl0NhfjQlddMMMVvZf5KB/3TsJZRuFXUfWpxCYJIDxAmed6YzqYCu9+1RVq43SXIX0n8ASoEjuBwI+CW75j/fWUl2CetHAkCPxfVDHdQ+ZksHzisYuUTMntFjelQb9wIDAQAB
