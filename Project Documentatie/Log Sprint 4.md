## Log maandag 10 Juli 2023

### Dagverslag:
Vandaag bezig geweest met het werkende krijgen van de omschakeling van HTTP naar HTTPS. In de ochtend het certificaat werkende gekregen.

### Obstakels:
Ik had het probleem dat na het overschakelen naar HTTPS de Health Checks van de instances niet meer wilde lukken, waardoor er constand instances werden aangemaakt en vervolgens weer geterminate.

### Oplossingen:
Na goed te hebben nagedacht over de architectuur en logica van wat ik wilde, en na een interactief rubber-ducky moment bij de Q&A met Casper, was bevestigd dat niet álles HTTPS kon zijn, omdat het certificaat op de LB stond, en niet op de instance. Na dit te hebben geïmplementeerd in mijn code werkte alles goed.

### Learnings:
De problemen zijn niet altijd de code, maar soms is het wat je er mee wil doen wat niet logisch is.

---
