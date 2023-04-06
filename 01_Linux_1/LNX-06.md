# Telnet daemon status veranderen.

## Key-terms
**Telnet**: Een verouderde, onveilige manier om verbinding te maken met een ander apparaat. De data wordt onbeveiligd als 'plain text' verzonden, dus erg onveilig. Het is vervangen door SSH, wat gebruik maakt van encryptie.

**Daemon**: Een service die op de achtergrond draait. Je herkent ze aan de 'd' achter de naam van het proces. Bijv. systemd, httpd, telnetd.

**systemctl**: System Control. Een command waarmee je het systeem en services van systemd kan bekijken en beïnvloeden. Je kan de status van services en daemons bekijken, deze starten, stoppen en herstarten en instellen dat ze moeten opstarten met het systeem, of juist niet.

**systemd**: Het allereerste proces wat Linux draait. Alle daemons worden door systemd gestart.


## Opdracht
De opdracht was om de telnet daemon te starten, de PID te vinden, te kijken hoeveel geheugen het gebruikt en de daemon weer te stoppen.

### Gebruikte bronnen
https://www.digitalocean.com/community/tutorials/telnet-command-linux-unix

### Ervaren problemen
Het grootste probleem was het uitvinden welke daemon gebruikt moest worden. De telnet daemon kon niet worden aangesproken, enkel te zien via  ```ps -aux | grep telnetd```.
Na veel zoeken en overleg kon het niet anders zijn dat de inetd daemon. Daarna ging de opdracht zonder moeite.

### Resultaat
Screenshot [LNX-06.png](/00_includes/LNX-06.png) staat in de 00_includes map.

![](/00_includes/LNX-06.png)
