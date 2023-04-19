Leren werken met nmap en meer oefening met Wireshark

## Key-terms
### nmap:
Een programma die netwerkscans kan maken.

### Wireshark:
Een programma die packets kan bekijken die door jouw apparaat worden verstuurd en ontvangen.

## Opdracht
- Scan het netwerk van de Linux VM, wat vind je?
- Open Wireshark op je PC en start een browser. Wat zie je gebeuren? (zet Zoom uit om niet overspoeld te worden met traffic.)

### Gebruikte bronnen
[nmap commands:](https://www.networkworld.com/article/3314832/using-nmap-on-your-home-network.html)

### Ervaren problemen
Geen.

### Resultaat
Ik heb met het commando `nmap -sn 10.171.154.0/24` een overzicht gekregen van de VMs van de medecursisten op het netwerk en hun IP-adres.
Screenshot staat in de 00_includes folder onder [SEC-01.png](/00_includes/SEC-01.png).

![](/00_includes/SEC-01.png)  

Met Wireshark heb ik een scan gedaan wanneer ik mijn browser opstart. Te verwachten was dat er, aangezien ik veel tabs open heb, er heel veel HTTPS berichten over het netwerk gingen. Bij mij gingen deze echter naar hetzelfde adres, omdat ik achter een VPN zit.
