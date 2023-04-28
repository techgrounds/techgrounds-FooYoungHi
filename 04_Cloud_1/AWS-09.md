# Shared Responsibility Model.
Wat is het en hoe wekrt dat bij AWS.

## Key-terms
### Shared Responsibility Model:
Een model dat aangeeft welke partij waar verantwoordelijk voor is.  
AWS is verantwoordelijk voor de cloud zelf, en de klant is verantwoordelijk voor alles wat ze *in* de cloud zetten.  

Waar AWS voor verantwoordelijk is, is de fysieke hardware en de infrastructuur die ze gebruiken. Ook het beveiligen van de datacenters zelf hoort hierbij. Ook zijn ze verantwoordelijk voor de backend(host OS, virtualisation layer), waar de klanten gebruik van maken.

De klanten zijn verantwoordelijk voor alles wat ze in de cloud zetten. Als je een EC2 instance aanmaakt, ben je zelf verantwoordelijk voor het beveiligen daarvan. Maak je een VPC, dan ben je verantwoordelijk voor de veiligheid daarvan. Zet je iets in een S3, dan is het aan jou om dat te encrypten.
Wat precies de verantwoordelijkheid is van de klant en van AWS, hangt af van de service. Voor sommige services heeft AWS zelf de meeste verantwoordelijkeid, voor andere de gebruiker.

## Opdracht
### Bestudeer:
- Het AWS Shared Responsibility Model.

### Gebruikte bronnen
[AWS:](https://aws.amazon.com/compliance/shared-responsibility-model/)

### Ervaren problemen
Geen.

### Resultaat
Zie Key-terms.
