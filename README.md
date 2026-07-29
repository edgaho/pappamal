# Holm &amp; Eventyr

Eventyr og fortellinger for barn — norrøne myter, folkeeventyr og hjemmelagede historier.

Laget for to lesere på 4 og 7 år, og for en iPad på sengekanten. Ingen reklame, ingen sporing,
ingen innlogging. Bare tekst som er stor nok til å leses høyt.

## Se den lokalt

Åpne `index.html` i en nettleser — det er alt som trengs. Vil du ha en ekte server:

```bash
npx serve .
```

## Hva som er her

| Kategori | Ferdige | På vei |
| --- | --- | --- |
| Norrøne fortellinger | 2 | 3 |
| Antikken | 0 | 1 |
| Folkeeventyr | 0 | 2 |
| Hjemmelagede | 0 | — |

Ferdige fortellinger:

- **Odin og jotnen som kunne alle svarene** — fritt etter Vavtrudnesmål, Den eldre Edda. 6–9 år.
- **Tor og dvergen som visste alt** — fritt etter Alvismål, Den eldre Edda. 4–9 år.

Hver fortelling har en seksjon **«For nysgjerrige foreldre»** nederst: hva som er tro mot kilden,
hva som er endret, hva som er diktet til, og hva som er tonet ned.

## Struktur

```
index.html                  forsiden — fire kategorier + ferdige fortellinger
kategorier/*.html           én side per kategori
fortellinger/*.html         én side per fortelling
assets/style.css            hele designet
assets/app.js               kveldsmodus + tekststørrelse (lagres i nettleseren)
```

Ingen byggesteg, ingen avhengigheter. En ny fortelling er én ny HTML-fil kopiert fra en
eksisterende, pluss en lenke fra kategorisiden.

## Design

Parchment-bakgrunn, kullsvart-grå tekst, dempet gull, skogsgrønn og burgunder. Overskrifter i
Cormorant Garamond, brødtekst i Lora, grensesnitt i Inter. Én spalte, maks 680 px.
Kveldsmodus følger systemet og kan overstyres. Tekststørrelsen kan skrus opp til 30 px.

## Publisering

**GitHub Pages** — workflowen i `.github/workflows/pages.yml` publiserer `main` automatisk.
Skru på én gang under *Settings → Pages → Source: GitHub Actions*.

**Vercel** — `vercel.json` ligger klar. Koble repoet i Vercel-dashbordet, eller kjør `vercel`.

## Kildene

Alle fortellinger er fritt adaptert fra tekster som er falt i det fri. Kildene står oppgitt på
hver enkelt side, med lenker til originalene.
