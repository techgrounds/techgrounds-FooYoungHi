# Functions
Leren werken met functions

## Key-terms


## Opdracht
### Opdracht 1:
- Maak een nieuw script.
- import de *random* package.
- print 5 verschillende integers met een waarde tussen 0 en 100

### Opdracht 2:
- Maak een nieuw script.
- maak de custom functon 'myfunction() die "Hello, World!" print.
- roep myfunction aan.
- Herschrijf je fuctie zodat het een string als input kan gebruiken. De ouput moet neerkomen op "Hello, `<input>`" .

### Opdracht 3:
- Maak een nieuw script.
- Kopiëer de volgende code:  
	```
	def avg():
		# write your code here
		
		# you are not allowed to edit any code below here
		x = 128
		y = 255
		z = avg(x,y)
	print("The average of",x,"and",y,"is",z)
``
- Schijf de custum avg() function dusdanig dat deze het gemiddelde uitrekent en toont. Je mag niet de code wijzigen onder de tweede comment.


### Gebruikte bronnen
Open-Assistant.io

### Ervaren problemen
Bij oefening 3 zag ik dat het gemiddelde, 191.5, een float moest zijn, maar wat ik ook deed, ik bleef 191 of 191.0 zien. Ook na 'overleg' met Open Assistant kwam ik er niet uit. Bij navraag aan Casper bleek de fout bijzonder simpel te zijn. Ik maakte gebruik van de `//` operator in plaats van de `/` operator, waardoor ik een *floor division* gebruikte. Dit is een afronding van de deling.

### Resultaat
#### Opdracht 1:
Screenshot en de code staan in de 00_includes folder als [PRG-06-1.png](/00_includes/PRG-06-1.png) en [PRG-06-1.py](/00_includes/PRG-06-1.py).  
![PRG-06-1.png](/00_includes/PRG-06-1.png)  

#### Opdracht 2:
Screenshot en de code staan in de 00_includes folder als [PRG-06-2.png](/00_includes/PRG-06-2.png) en [PRG-06-2.py](/00_includes/PRG-06-2.py).  
![PRG-06-2.png](/00_includes/PRG-06-2png)  

#### Opdracht 3:
Screenshot en de code staan in de 00_includes folder als [PRG-06-3.png](/00_includes/PRG-06-3.png) en [PRG-06-3.py](/00_includes/PRG-06-3.py).  
![PRG-06-3.png](/00_includes/PRG-06-3.png)  
