# Pappamål

> Å forstå verden med eventyr

Gudene i Edda krangler, lurer hverandre og angrer — og det er nettopp derfor de er så gode å tenke
med. Loke gjorde minst like mye godt som vondt, og Tyr la hånden i ulvens munn fordi noen måtte.
Her er de fortalt videre, med all begeistringen de fortjener.

Laget for lesere på 4 og 7 år, og for en iPad ved sengekanten. Ingen reklame, ingen sporing, ingen
innlogging. Bare tekst som er stor nok til å leses høyt. Bruk den gjerne hjemme hos deg også.

## Navnet

Eddaens diktnavn sier hvem ordene kommer fra: Vavtrudnesmål er jotnens, Alvismål er dvergens,
Håvamål er Odins. Håvamål er samtidig det diktet som handler om hvordan man lever — hvordan man er
mot venner, mot fremmede, mot seg selv. Det er den jobben eventyrene gjør når de leses høyt, og det
er derfor navnet ble hetende noe på `-mål`.

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

- **Odin og jotnen som kunne alle svarene** — fritt etter Vavtrudnesmål, Den eldre Edda. 6–9 år.
- **Tor og dvergen som visste alt** — fritt etter Alvismål, Den eldre Edda. 4–9 år.

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
