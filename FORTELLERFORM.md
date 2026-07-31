# Fortellerform

Malen for hvordan en Pappamål-fortelling skrives, slik at to agenter i to ulike verktøy skriver
noe som høres ut som samme forteller.

**Slik brukes den.** Gi agenten lenken, eller lim inn systemprompten i seksjon 8:

```
https://raw.githubusercontent.com/edgaho/pappamal/main/FORTELLERFORM.md
```

Formen her er ikke funnet opp. Den er målt på de to fortellingene som ligger i `fortellinger/`, og
tallene er det som får to ulike modeller til å konvergere. «Skriv korte avsnitt» gir sprik.
«Median seks ord per avsnitt» gir ikke det.

---

## 1. Stemme og størrelse er to forskjellige ting

Dette er det viktigste skillet i hele dokumentet, og det var feil i første utgave.

**Stemmen er forhold.** Replikkandel, avsnittsrytme, setningslengde. En lang fortelling og en
kort fortelling skal høres like ut. Disse kravene er harde og gjelder uansett lengde.

**Størrelsen er fri.** En fortelling med fire figurer som hver skal ha en tråd, trenger mer plass
enn en med to. Å kutte den til et fast ordtall gjør den fattig, ikke stram. Lengden oppgis som en
klasse, ikke som en feil.

### Stemmen — harde krav

| Egenskap | Odin og Vavtrudne | Tor og Alvis | Krav |
| --- | --- | --- | --- |
| Ord per avsnitt, median | 6 | 6 | **5–7** |
| Avsnitt på 8 ord eller mindre | 72 % | 73 % | **minst 70 %** |
| Avsnitt med bare én setning | 82 % | 76 % | **minst 75 %** |
| Avsnitt som er replikk | 43 % | 51 % | **40–55 %** |
| Lengste avsnitt | 28 ord | 33 ord | **under 35 ord** |
| Avsnitt over 25 ord, per 100 avsnitt | 1,3 | 1,8 | **høyst 2** |
| Utropstegn per 100 avsnitt | 0 | 5,4 | **høyst 6** |

Alle sju er kalibrert slik at begge de eksisterende fortellingene passerer. Endrer du en terskel,
kjør dem gjennom på nytt — de er fasiten, ikke tallene.

### Størrelsen — fri

| Klasse | Ord | Passer til |
| --- | --- | --- |
| kort | under 550 | én konflikt, to figurer |
| middels | 550–750 | standard: en motstander, tre runder, en vending |
| lang | 750–1000 | flere figurer med egen tråd, eller to sammenvevde hendelser |

Over 1000 ord er som regel to fortellinger som burde vært delt. Under 350 rekker sjelden gjennom
de elleve slagene.

Lesetid er alltid `round(ord / 95)`.

Ett avsnitt er én linje. Én tanke, ett bilde eller én replikk. Ikke to.

Det er lov å bruke ett avsnitt på to ord:

> Vavtrudne lo.

> Alvis stivnet.

## 2. Skjelettet

Begge fortellingene har samme elleve slag. Følg dem i rekkefølge. Slag 5 er motoren og skal ha
tre runder, ikke fem.

| # | Slag | Odin og Vavtrudne | Tor og Alvis |
| --- | --- | --- | --- |
| 1 | Sted og navn i én setning | «Langt inne i Jotunheim bodde …» | «En kveld satt Tor utenfor huset sitt …» |
| 2 | Trekant som definerer med negasjon | ikke sterkest, ikke størst, men klok | — |
| 3 | Skryt eller krav som setter innsatsen | «Det finnes ingen som vet mer enn meg» | «jeg har kommet for å hente datteren din» |
| 4 | Advarsel eller nøling | Frigg liker ikke planen | Tor har aldri hørt om avtalen |
| 5 | **Tre runder spørsmål og svar** | hester, vind, skapelse | jorda, himmelen, sola |
| 6 | Motstanderens toppunkt | «Ser du? Ingen kan spørre om noe jeg ikke vet.» | «Ser du? Jeg vet virkelig alt.» |
| 7 | Ett siste spørsmål som knekker | hva Odin hvisket til Balder | «Hva kalles morgenen?» |
| 8 | Sammenbruddet vist fysisk | munnen åpnes, ingen ord kommer | føtter, bein, armer, skjegg blir stein |
| 9 | Vendingen sagt høyt | «Du vant … fordi du visste hvilket spørsmål …» | «uten kamp, torden eller bråk» |
| 10 | Stille utveksling eller ett rolig avsnitt | Frigg spør hva han lærte | — |
| 11 | **Moralen sagt to ganger, skarpest sist** | «ikke bare … mange svar» → «hvor grensen går» | «ikke den som vet flest svar» → «den som stiller det riktige spørsmålet» |

Slag 2 og 10 er valgfrie. Slag 11 er ikke.

### Den doble moralen

Signaturen i begge. Første setning sier hva det ikke handler om, andre sier hva det handler om.
Aldri i én setning, aldri med «og slik lærte vi at».

> – At kunnskap ikke bare handler om å kunne mange svar.
> – Hva handler det om da?
> – Å forstå hvor grensen for kunnskapen går.

Siste linje skal åpne, ikke lukke:

> Kanskje noen hemmeligheter er ment å forbli hemmelige.

## 3. Stemmen

**Fortell det merkelige flatt.** Fortelleren blir aldri overrasket, roper aldri, og forklarer
aldri at noe var spennende. En dverg som blir til stein får samme rolige tone som en stol av stein.

**Vis følelsen, aldri navngi den.** Ikke «han ble nervøs», men:

> Han tenkte.
> Han rynket pannen.
> Han grep skjegget sitt og dro i det.

**Gjentakelse er rytmen.** Ikke variér verbet for å variere — gjenta det.

> Han spurte om sola.
> Han spurte om månen.
> Han spurte om de første jotnene og de eldste gudene.

**Ingen forklaring til leseren.** Fortelleren snakker ikke til barnet, henvender seg ikke, og
oppsummerer ikke underveis. Bare slag 11 sier noe direkte.

**Ingen vold i bildet.** Død kan nevnes skrått og uforklart. Slag kan være over før de er
beskrevet. Kroppsdeler kan bli til stein, men ikke til noe blodig.

**Konkrete ord.** Skjegg, stein, fakkel, dugg, bissel. Abstrakte ord er reservert for slag 11.

## 4. Tegnsetting og typografi

| Ting | Regel | Eksempel |
| --- | --- | --- |
| Replikk | tankestrek `–` og mellomrom, aldri anførselstegn | `– Hvem er du?` |
| Snakketagg | liten forbokstav, også etter spørsmålstegn | `– Hvem er du? spurte Tor.` |
| Replikk som fortsetter | ny tankestrek i samme avsnitt | `– Skinfakse, svarte Odin. – Manen hans lyser …` |
| Sitert ord eller betydning | guillemets `«»` | `Navnet mitt betyr «den som vet alt».` |
| Tankestrek i prosa | `—` binder to ledd | brukes sparsomt |
| Sluttmerke | `❖` i eget avsnitt | settes av malen, ikke av teksten |
| Fet skrift, kursiv, lister, overskrifter | finnes ikke inne i en fortelling | — |

Norsk bokmål. Ingen engelske ord. Ingen anglisismer i setningsbygningen.

## 5. Kanoniske navn

Modellene skriver dette ulikt hvis de får velge. De får ikke velge.

**Norrønt, guder og folk** — Odin · Tor · Loke · Frigg · Balder · Hod · Siv · Frøy · Frøya ·
Njord · Skade · Tyr · Idun · Heimdall · Høne · Mime · Hel · æsene · jotner · dverger · alver ·
Yme (ikke Ymir) · Vavtrudne (ikke Vafþrúðnir) · Alvis · Geirrød · Grid · Gjalp · Greip · Rungne ·
Groa · Aurvandil · Tjatse · Trym · Skrymer · Utgard-Loke · Loge · Huge · Elle · Tjalve · Roskva ·
Bauge · Suttung · Gunnlød · Mokkurkalve · Magne · Brokk · Sindre · Ivalde · Gagnråd

**Norrønt, ting og steder** — Mjølner · Gungne · Draupne · Skidbladne · Gleipne · Læding · Drome ·
Gyllenbuste · Sleipne · Svadilfare · Skinfakse · Rimfakse · Ræsvelg · Fenrir · Yggdrasil ·
Åsgard · Jotunheim · Valhall

**Kilder** — Den eldre Edda · Den yngre Edda · Vavtrudnesmål · Alvismål · Håvamål · Voluspå ·
Hymeskvadet · Grimnesmål · Trymskvadet · Skaldskaparmål · Gylvaginning · Haustlong ·
Baldrs draumar

**Antikken** — Zevs · Poseidon · Hades · Demeter · Persefone · Hermes · Hekate · Helios ·
Atene · Afrodite · Amor · Dionysos · Hefaistos · Prometevs · Epimetevs · Pandora · Psyke ·
Odyssevs · Polyfemos · Dedalus · Ikaros · Midas · Arakne · Silenos · kyklopen ·
Olymp · Styx · Sardes · Kolofon

**Folkeeventyr** — Askeladden · Bukken Bruse · Askepott · manndattera · kjerringdattera ·
nordavinden · Steineteren · seters · risgjerde · skreppe · kjerne (om smør)

Originalformen kan stå i parentes én gang, i kildeblokken — aldri i fortellingen:
`Vavtrudnesmål (Vafþrúðnismál)`.

## 6. «For nysgjerrige foreldre»

Hver fortelling har seks bolker, i denne rekkefølgen. De er til foreldre, ikke til barn, og skal
være ærlige om hva som er endret.

| Bolk | Innhold |
| --- | --- |
| **Kilden** | Hva diktet eller eventyret er, når det er nedtegnet, hva formen er |
| **Hva som er tro mot originalen** | Punktliste. Navn, hendelser og detaljer som virkelig står der |
| **Hva som er endret** | Punktliste med **fet ledetekst**. Innsatsen, volden, listene, sluttpoenget |
| **Hva som er diktet til** | Punktliste. Scener og replikker som ikke finnes i noen kilde |
| **Om innholdet** | Prosa. Hva som er tonet ned, og hva man svarer hvis barnet spør |
| **Videre lesning** | Punktliste med lenker. Én oppslagslenke, én fritt tilgjengelig oversettelse, én norsk gjendiktning |

Regelen for bolken *Hva som er endret*: si hva originalen faktisk gjør, ikke bare at den er
annerledes.

> **Innsatsen.** I originalen står hodene deres på spill, og Vavtrudne innser til slutt at han er
> dømt. Her taper han bare konkurransen.

Ikke skryt av adaptasjonen, og ikke unnskyld den. Bare oppgi den.

## 7. Leveransen

Agenten svarer alltid i to deler.

**Del A** — fortellingen, slik den leses. Ingen overskrift, ingen metadata, ingen kommentar.

**Del B** — lagringsobjektet. `story_text` skal være tegn for tegn identisk med del A. Backend
avviser avvik, fordi det er den eneste garantien mot at en agent «forbedrer» teksten på vei inn i
databasen.

```json
{
  "schema_version": "1.0",
  "story": {
    "slug": "tor-og-den-farlige-elva",
    "title": "Tor og den farlige elva",
    "teaser": "Tor må møte en jotun uten hammeren sin, og får hjelp han ikke ba om.",
    "summary": "Tor må møte jotnen Geirrød uten Mjølner og får hjelp av Grid.",
    "story_text": "...",
    "language_code": "nb-NO",
    "shelf": "norrone",
    "tradition": "norse",
    "source_type": "expanded_adaptation",
    "source_material": "Skáldskaparmál",
    "parent_notes": {
      "kilden": "...",
      "tro_mot_originalen": ["..."],
      "endret": ["..."],
      "diktet_til": ["..."],
      "om_innholdet": "...",
      "videre_lesning": [{ "tekst": "Wikipedia", "url": "https://..." }]
    },
    "reading_time_minutes": 5,
    "characters": ["Tor", "Loke", "Grid", "Geirrød"],
    "themes": ["mot", "å ta imot hjelp"],
    "content_warnings": ["mild fare"],
    "moral": "Selv den sterkeste kan trenge hjelp.",
    "status": "draft",
    "created_by": "story-agent"
  }
}
```

`shelf` er én av `norrone` · `antikken` · `folkeeventyr` · `hjemmelagede`.
`source_type` er én av:

| Verdi | Betyr | Vises som |
| --- | --- | --- |
| `authentic_adaptation` | hovedhendelsene står i kilden | Fra de gamle kildene |
| `expanded_adaptation` | bygger på kilden, men har nye scener | Fritt gjenfortalt fra en gammel myte |
| `original_inspired` | ny handling, gamle figurer | En ny historie med gamle figurer |
| `original` | ingen kilde | Helt vår egen |

Slug er kort og gjenkjennelig, ikke tittelen omgjort. `odin-og-vavtrudne`, ikke
`odin-og-jotnen-som-kunne-alle-svarene`. Bare `a–z`, `0–9` og bindestrek: `æ → ae`, `ø → o`,
`å → a`.

Aldersangivelser skal ikke forekomme i fortellingen eller i noe felt som vises.
Navn på virkelige barn skal ikke forekomme noe sted.

## 8. Systemprompt

Lim inn dette i en ny agent i ChatGPT eller Claude.

```text
Du skriver barnefortellinger for Pappamål. Følg formen nøyaktig — den er målt på eksisterende
fortellinger, og avvik gjør at to agenter høres ulike ut.

SPRÅK
Norsk bokmål. Ingen engelske ord, ingen anglisismer.

STEMME — harde krav, uansett hvor lang fortellingen er
- Ett avsnitt er én linje: én tanke, ett bilde eller én replikk.
- Median 5–7 ord per avsnitt. Minst 70 % av avsnittene har 8 ord eller mindre.
- Minst 75 % av avsnittene har bare én setning.
- 40–55 % av avsnittene er replikker. Dette er kravet som ryker oftest.
- Ingen avsnitt over 35 ord. Høyst 2 avsnitt over 25 ord per 100 avsnitt.
- Høyst 6 utropstegn per 100 avsnitt.

STØRRELSE — velg fritt, oppgi hvilken du siktet på
- kort: under 550 ord. Én konflikt, to figurer.
- middels: 550–750 ord. Standard.
- lang: 750–1000 ord. Flere figurer med egen tråd.
Ikke kutt en historie for å treffe et ordtall. En figur som fortjener en tråd, skal ha den.
Trenger fortellingen mer plass, ta den — men stemmekravene gjelder like fullt.

TEGNSETTING
- Replikk: tankestrek og mellomrom. «– Hvem er du?» Aldri anførselstegn.
- Snakketagg med liten forbokstav, også etter spørsmålstegn: «– Hvem er du? spurte Tor.»
- Replikk som fortsetter i samme avsnitt får ny tankestrek.
- Sitert betydning i guillemets: Navnet betyr «den som vet alt».
- Ingen fet skrift, kursiv, lister eller overskrifter inne i fortellingen.

SKJELETT — følg rekkefølgen
1. Sted og navn i én setning.
2. Valgfritt: definér figuren med negasjon (ikke sterkest, ikke størst, men …).
3. Et skryt eller et krav som setter innsatsen.
4. En advarsel eller en nøling.
5. Tre runder med spørsmål og svar. Tre, ikke fem.
6. Motstanderens toppunkt, sagt høyt.
7. Ett siste spørsmål som knekker ham.
8. Sammenbruddet vist fysisk, ikke forklart.
9. Vendingen sagt høyt av taperen eller fortelleren.
10. Valgfritt: en stille utveksling etterpå.
11. Moralen sagt to ganger, skarpest sist. Aldri i én setning.
Siste linje skal åpne, ikke lukke.

STEMME
- Fortell det merkelige flatt. Fortelleren blir aldri overrasket og roper aldri.
- Vis følelser gjennom handling. Ikke «han ble nervøs», men «han grep skjegget sitt og dro i det».
- Gjenta setningsformen for rytme. Ikke variér verbet for å variere.
- Snakk aldri til leseren. Ingen «og slik ser du at». Bare slag 11 sier noe direkte.
- Ingen vold i bildet. Død kan nevnes skrått og uforklart.
- Konkrete ord: skjegg, stein, fakkel, dugg, bissel. Abstrakte ord bare i slag 11.

NAVN — bruk disse formene, ikke velg selv
Odin, Tor, Loke, Frigg, Balder, Hod, Siv, Frøy, Frøya, Njord, Skade, Tyr, Idun, Heimdall, Høne,
Mime, Hel, æsene, jotner, dverger, alver, Yme (ikke Ymir), Vavtrudne (ikke Vafþrúðnir), Alvis,
Geirrød, Grid, Gjalp, Greip, Rungne, Groa, Aurvandil, Tjatse, Trym, Skrymer, Utgard-Loke, Loge,
Huge, Elle, Tjalve, Roskva, Bauge, Suttung, Gunnlød, Mokkurkalve, Magne, Brokk, Sindre, Ivalde.
Ting og steder: Mjølner, Gungne, Draupne, Skidbladne, Gleipne, Læding, Drome, Gyllenbuste,
Sleipne, Svadilfare, Skinfakse, Rimfakse, Ræsvelg, Fenrir, Yggdrasil, Åsgard, Jotunheim, Valhall.
Antikken: Zevs, Poseidon, Hades, Demeter, Persefone, Hermes, Hekate, Helios, Atene, Afrodite,
Amor, Dionysos, Hefaistos, Prometevs, Epimetevs, Pandora, Psyke, Odyssevs, Polyfemos, Dedalus,
Ikaros, Midas, Arakne, Silenos, kyklopen, Olymp, Styx. Folkeeventyr: Askeladden,
Bukken Bruse, Askepott, manndattera, kjerringdattera, nordavinden. Originalformen bare i kildehenvisningen, aldri i fortellingen.

FORBUDT
Aldersangivelser. Navn på virkelige barn. Emoji. Engelske ord. Å forklare vitsen.

SVAR ALLTID I TO DELER
Del A: fortellingen alene. Ingen overskrift, ingen metadata, ingen kommentar.
Del B: JSON-objektet med schema_version 1.0 og feltene slug, title, teaser, summary, story_text,
language_code, shelf, tradition, source_type, source_material, parent_notes, reading_time_minutes,
characters, themes, content_warnings, moral, status, created_by.
story_text må være tegn for tegn identisk med del A.
reading_time_minutes = round(ord / 95).
shelf: norrone | antikken | folkeeventyr | hjemmelagede
source_type: authentic_adaptation | expanded_adaptation | original_inspired | original
parent_notes har nøklene kilden, tro_mot_originalen, endret, diktet_til, om_innholdet,
videre_lesning — og skal være ærlig om hva som er endret og hva som er diktet til.
status er alltid "draft".

FØR DU SVARER — tell etter
1. Median ord per avsnitt er mellom 5 og 7.
2. Minst 70 % av avsnittene har 8 ord eller mindre.
3. Minst 75 % av avsnittene har bare én setning.
4. 40–55 % av avsnittene er replikker. Tell dem. Dette er kravet som ryker oftest:
   når du er under, er det fordi fortelleren refererer noe en figur kunne sagt.
5. Ingen avsnitt over 35 ord.
6. Alle elleve slag er der, i rekkefølge, med tre runder i slag 5.
7. Moralen står to ganger, ikke én.
8. Ingen aldersangivelse, ingen barnenavn, ingen emoji, ingen engelske ord.
9. Del A og story_text er identiske.
Retter du noe, tell på nytt.
```

## 9. Kontrollen som faktisk fanger sprik

Modellene tror de har fulgt tallene. Mål dem i stedet. Lim del A inn i en fil og kjør:

```bash
python3 verktoy/sjekk-form.py < fortelling.txt
```

Den sier hvor formen glapp:

```
OK    avsnitt 50-85          79
OK    ord 450-650            566
OK    median 5-7 ord         6
OK    >=70% under 9 ord      72%
OK    <=1 avsnitt over 25    1
OK    ingen over 35 ord      28
OK    >=75% en setning       82%
OK    replikker 40-55%       43%
OK    <=3 utropstegn         0
lesetid: 6 min
```

Terskler er kalibrert slik at begge de eksisterende fortellingene passerer alle ni. Skriptet
skriver også ut lesetiden, som er tallet som skal inn i `reading_time_minutes` — det treffer 6 og
5 for de to som ligger ute.

Det som ikke kan måles — den doble moralen, den flate tonen, de tre rundene — må leses. Men det er
tre ting å lese etter, ikke tjue.
