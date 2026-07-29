# Pappamål

> Å forstå verden med eventyr

Gudene i Edda krangler, lurer hverandre og angrer — og det er nettopp derfor de er så gode å tenke
med. Loke gjorde minst like mye godt som vondt, og Tyr la hånden i ulvens munn fordi noen måtte.
Her er de fortalt videre, med all begeistringen de fortjener.

Laget for høytlesning, og for en iPad ved sengekanten. Ingen reklame, ingen sporing, ingen
innlogging. Bare tekst som er stor nok til å leses høyt. Bruk den gjerne hjemme hos deg også.

## Om navnet

Eddaens dikt heter det de heter fordi navnet sier hvem ordene kommer fra. Vavtrudnesmål er jotnens,
Alvismål er dvergens, Håvamål er Odins. Håvamål er samtidig diktet om hvordan man lever, og det er
den delen vi har hatt mest bruk for.

Gudene er ikke store forbilder. De gjør dumme ting, de angrer, og de kommer seg videre. Det gjør dem
lette å ta fram når noe er vanskelig — det er kortere vei til «husker du at Tyr visste at det ville
koste ham hånden, og gjorde det likevel?» enn til å forklare mot fra grunnen av.

Vi har hatt tunge perioder, som alle har. Fortellingene har hjulpet oss gjennom flere av dem, ikke
fordi de gir svar, men fordi de gir noe å snakke gjennom. Og fordi de er til å bli begeistret av:
det er lov å synes at en dverg som blir til stein er det morsomste som finnes, samme hvilken uke det
er.

Derfor «-mål». Ordene kommer fra en pappa, ikke fra en gud — det er hele forklaringen.

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
