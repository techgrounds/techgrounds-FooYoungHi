# Een SSH connectie maken met Linux

## Key-terms
SSH: *S*ecure *Sh*ell. Een protocol om veilig een verbinding te maken met een apparaat op afstand.

## Opdracht
De opdracht was om een SSH connectie te maken met de VM en met je username te achterhalen met het 'whoami' command.

### Gebruikte bronnen
https://www.nixcraft.com/t/permissions-0664-for-home-user-ssh-file-pem-are-too-open-for-ssh/2591
https://linuxiac.com/ssh-to-port-other-than-22/

### Ervaren problemen
Het inloggen met .pem was even een issue, omdat hij aangaf dat de file 'too open' was en het dus negeerde.
Na een chown 0600 bestandsnaam.pem te hebben uitgevoerd in de terminal kon ik zo inloggen.

### Resultaat
Ik kon inloggen op de VM en met de command de user 'danny' geverifiëerd.
Screenshot [LNX-01.png](/00_includes/LNX-01.png) staat in de 00_includes folder. 
![LNX-01.png](/00_includes/LNX-01.png)
