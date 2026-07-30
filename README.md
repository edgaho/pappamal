# Pappamål

> Å forstå verden med eventyr

Gudene krangler, lurer hverandre og angrer — og det er nettopp derfor de er så gode å tenke med.
Loke gjorde minst like mye godt som vondt, og Prometevs ga menneskene ilden selv om han visste hva
det ville koste ham. Her er de fortalt videre, med all begeistringen de fortjener.

Laget for høytlesning, og for en iPad ved sengekanten. Ingen reklame, ingen sporing, ingen
innlogging. Bare tekst som er stor nok til å leses høyt. Bruk den gjerne hjemme hos deg også.

## Hvorfor det ligger her

På sengekanten hos noen små viking-folk har disse fortellingene vært noe av det fineste å dele. Ikke
som leggetidspensum, men som noe å bli begeistret over sammen — og etter hvert som noe å ta fram når
noe var vanskelig.

For gudene er ikke store forbilder. De gjør dumme ting, de angrer, og de kommer seg videre. Og
heltene er sjelden sterke: Psyke fikk en umulig haug korn å sortere og klarte det bare fordi maurene
hjalp henne, lenge før Askepott fikk fuglene sine. Det er kortere vei til den slags enn til å
forklare fra grunnen av at ingen må klare alt alene. Det er også lov å synes at en dverg som blir til
stein er det morsomste som finnes, samme hvilken uke det er.

Fortellingene er gamle — noen tusener av år, andre knapt to hundre — og de tilhører ingen. Det er
hele grunnen til at de ligger åpent her. Kanskje noen finner én å lese høyt i kveld, og kanskje det
blir en samtale, en vits som går igjen, eller et ritual som blir deres eget. Det er verdt mer enn
teksten.

## Om navnet

Eddaens dikt heter det de heter fordi navnet sier hvem ordene kommer fra: Vavtrudnesmål er jotnens,
Alvismål er dvergens, Håvamål er Odins. Håvamål er samtidig diktet om hvordan man lever, og det er
den delen vi har hatt mest bruk for. Navnet er ikke mer enn det — ordene kommer fra en pappa, ikke
fra en gud.

## Se den lokalt

Åpne `index.html` i en nettleser — det er alt som trengs. Vil du ha en ekte server:

```bash
npx serve .
```

## Hva som er her

| Hylle | Skrevet ned | Bare fortalt |
| --- | --- | --- |
| Norrøne fortellinger | 2 | 3 |
| Antikken | 0 | 1 |
| Folkeeventyr | 0 | 2 |
| Hjemmelagede | 0 | — |

Skrevet ned:

- **Odin og jotnen som kunne alle svarene** — fritt etter Vavtrudnesmål, Den eldre Edda.
- **Tor og dvergen som visste alt** — fritt etter Alvismål, Den eldre Edda.

Hver fortelling har en seksjon **«For nysgjerrige foreldre»** nederst: hva som er tro mot kilden,
hva som er endret, hva som er diktet til, og hva som er tonet ned.

## Skrive en ny fortelling

Formen er dokumentert og målbar i [FORTELLERFORM.md](FORTELLERFORM.md): elleve slag, målte
avsnittstall, kanoniske navn og en ferdig systemprompt til å lime inn i en agent. Mål resultatet
med:

```bash
python3 verktoy/sjekk-form.py < fortelling.txt
```

## Struktur

```
index.html                  forsiden — fire hyller + det som er skrevet ned
kategorier/*.html           én side per hylle
fortellinger/*.html         én side per fortelling
assets/style.css            hele designet
assets/app.js               kveldsmodus + tekststørrelse (lagres i nettleseren)
```

Ingen byggesteg, ingen avhengigheter. En ny fortelling er én ny HTML-fil kopiert fra en
eksisterende, pluss en lenke fra hyllesiden.

## Design

Parchment-bakgrunn, kullsvart-grå tekst, dempet gull, skogsgrønn og burgunder. Overskrifter i
Cormorant Garamond, brødtekst i Lora, grensesnitt i Inter. Én spalte, maks 680 px.
Kveldsmodus følger systemet og kan overstyres. Tekststørrelsen kan skrus opp til 30 px.

## Publisering

**GitHub Pages** — workflowen i `.github/workflows/pages.yml` publiserer `main` automatisk.
Live på [edgaho.github.io/pappamal](https://edgaho.github.io/pappamal/).

**Vercel** — `vercel.json` ligger klar. Koble repoet i Vercel-dashbordet, eller kjør `vercel`.

## Kildene

Alle fortellinger er fritt adaptert fra tekster som er falt i det fri. Kilden står oppgitt på hver
enkelt fortelling, med lenker til originalene.
