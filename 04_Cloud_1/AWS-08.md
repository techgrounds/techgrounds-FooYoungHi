# Security Groups
Begrijpen wat het is en hoe je er meer werkt.

## Key-terms

### Security Groups:
De AWS naam voor de firewall. Deze firewalls hebben alleen een 'explicit allow'. Alle poorten die niet gespecificeerd zijn worden standaard geblokkeerd.  
Het is een *stateful firewall* die in de VPC draait.  
Een SG kan meerdere instances ondersteunen en elke instance kan 5 SGs hebben.

### Network Access Control List, NACL:
Dit is een *stateless firewall* die op subnetniveau draait in de VPC.  Standaard staan *alle* poorten wagenwijd open voor het netwerk. Deze firewall heeft een *explicit allow- en deny lijst*.
Het is meer een firewall die de toegang beheert op het netwerk zelf, en niet het internet. Je kan toegang tot bepaalde applicaties blokkeren per user of groep, om de veiligheid van je netwerk te verbeteren.

## Opdracht
Bestudeer:
- Security groups in AWS.
- Network Access Control Lists in AWS.

### Gebruikte bronnen


### Ervaren problemen
Geen.

### Resultaat
Zie Key-Terms.
