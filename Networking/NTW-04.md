# Hexadecimal en Binary
Leren tellen in Hexadecimal en binary.

## Key-terms
### Hexadecimal:
Soms ook wel verkort *hex* genoemd, is een numeriek systeem dat 16 mogelijkheden heeft, waar ons decimale systeem daar 10 heeft. Het wordt ook wel omschreven als *base-16*.
Dit moet je niet verwarren met Ethernet snelheden, die ook met *BASE* worden beschreven.
Hex gaat van 0 tot 9, dan naar A-F
Als eerste getal zijn 0-9 vanzelfsprekend, maar na 9 komt geen 10, maar A.
Om het minder verwarrend te maken bij het lezen, wordt er vaak een '<sub>16</sub>' achter het getal gezet, om duidelijk te maken dat het om hexadecimaal gaat. Zo kan decimaal genoteerd worden met '<sub>10</sub>' achter het getal.

Decimaal | Hexadecimaal
--| --
1 |1
2|2
3|3
4|4
5|5
6|6
7|7
8|8
9|9
10|A
11|B
12|C
13|D
14|E
15|F

Zoals te zien gaat het vanaf 10 anders dan we gewend zijn om te tellen en kan het verwarrend worden. Zo is 10 in hex totaal iets anders dan 10 in decimaal. 10 in hex is 16 in decimaal. Hierdoor kan het verwarrend werken, omdat het totaal langs elkaar heen loopt.


**Van Hex naar Dec:**  
Voorbeeld: E0

16<sup>1</sup>|16<sup>0</sup>
--|--
E|0

E = 14 in decimaal, dus

16<sup>1</sup>|16<sup>0</sup>
--|--
14|0

van 16<sup>1</sup>  zijn er 14, dus 14 x 16  
van 16<sup>0</sup> zijn er 0, dus 0  
Decimaal is nu 14 x 16 + 0 = 224.

**Van Dec naar Hex:**
Voorbeeld: 
246

```
   16 / 246 \ 15
        16
        --
         86
         80
         --
          6
```

``` 246 / 16 = 15R6```  
R = Remaining; het getal dat overblijft dat je niet meer door 16 kan delen.  
Het getal dat achter de 'R' staat doen we nu even niets mee. Het getal dat vóór de 'R' staat gaan we weer proberen door 16 te delen.  
15 delen door 16 wordt een getal dat kleiner is dan 1. Wat we dan doen is het noteren als 0R15.  
``` 15 / 16 = 0R15```  
Nu hebben we 246 zoveel mogelijk gedeeld door 16, en hebben het genoteerd als  
```15R6```  
```0R15```  
In dit geval kunnen we de getallen vóór de 'R' weglaten. De getallen ná de 'R' moeten we van onder naar boven noteren. In bovenstaand geval dus als '15' '6' in decimaal.  
In hex: 15 = F, 6 = 6. De notatie is nu dus 'F6'.


### Binary:
Binary, of Binair in het Nederlands, is een ander cijfer systeem, waarbij exclusief met '0' en '1' wordt gewerkt. Binair betekent *tweevoudig*. Het wordt ook wel Base-2 genoemd.

is iets minder verwarrend als hexadecimaal, maar ook hier loop je tegen het punt op dat '10' iets totaal anders is. 10 in binair is 2 in decimaal.
Ook hierbij is het makkelijk door je zelf aan te leren, dat wanneer je in binair leest, bij bijvoorbeeld 10 niet 'tien' te lezen, maar 'één, nul'. Zet in je hoofd een spatie achter de cijfers om het makkeljker te lezen en niet in de war te raken. Ook wordt vaak '<sub>2</sub>' gebruikt om aan te geven dat het gaat om een binair getal.


**Van Binary naar Dec:**
Voorbeeld: 1101 1011

128|64|32|16|8|4|2|1
--|--|--|--|--|--|--|--
1|1|0|1|1|0|1|1|

128+64+16+8+2+1 = 219.


**Van Dec naar Binary:**
Het concept is hetzelfde, maar dan de ander kant op. Als we kijken naar bijvoorbeeld **228**, dan moeten we kijken naar het hoogste nummer dat er in 1 keer in kan. Na 128 komt 256 als extra '1', en daar kan 228 niet in, dus gaan we naar 128. Daar kan het 1x in, en zetten we onder de 128 een 1. Er blijft dan nog 228-128=100 over om te verdelen. 64 kan in 100, dus zetten we daar ook een 1. Dan blijft over 100-64=36. 32 kan in 36, dus gaat daar ook een 1. Nu is nog over 36-32=4. 4 kan uiteraard in 4, dus gaat daar de laatste 1. Onder de ongebruikte getallen komt een 0.

128|64|32|16|8|4|2|1
--|--|--|--|--|--|--|--
1|1|1|0|0|1|0|0


## Opdracht
Maak de onderstaande sommen. Zie Resultaat.

### Gebruikte bronnen
[Hexadecimal](https://www.youtube.com/watch?v=QJW6qnfhC70&ab_channel=TheOrganicChemistryTutor)  
Rekenen in binary kon ik al.

### Ervaren problemen
Geen.

### Resultaat
Decimal | Binary
--- | ---
16 | 0001 0000
128 |1000 0000
228 |1110 0100
112 | 0111 0000
73 | 0100 1001

Binary | Decimal
---| ---
1010 1010 | 170
1111 0000 | 240
1101 1011 | 219
1010 0000 | 160
0011 1010 | 58

Decimal | Hex
--- | ---
15 | 0F
37 | 25
246 | F6
125 | 7D
209 | D1

Hex | Decimal
-- | -
88 | 136
e0 | 224
cb | 203
2f | 47
d8 | 216
