#!/usr/bin/env python3
"""Bygg fortellingssider, hyllesider og forsidelista fra data/.

    python3 verktoy/bygg.py

Kilden er data/import-chatgpt.json pluss manifestet under. De to håndskrevne
fortellingene i fortellinger/odin-og-vavtrudne.html og tor-og-alvis.html blir
ikke rørt — bare forrige/neste-lenkene deres, siden hylla har blitt lengre.

Når Supabase kommer, byttes lasteren nederst. Malen er den samme.
"""

import html
import json
import os
import re

ROT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HYLLER = {
    'norrone':      ('Norrøne fortellinger', '--cat-norrone'),
    'antikken':     ('Antikken',             '--cat-antikken'),
    'folkeeventyr': ('Folkeeventyr',         '--cat-folke'),
    'hjemmelagede': ('Hjemmelagede',         '--cat-hjemme'),
}

KILDETYPE = {
    'authentic_adaptation': 'Fra de gamle kildene',
    'expanded_adaptation':  'Fritt gjenfortalt fra en gammel myte',
    'original_inspired':    'En ny historie med gamle figurer',
    'original':             'Helt vår egen',
}

KILDEBLOKK = {
    'authentic_adaptation': 'Basert på <strong>{k}</strong>. Fritt adaptert for barn.',
    'expanded_adaptation':  'Fritt gjenfortalt fra <strong>{k}</strong>. Adaptert for barn, med scener som ikke står i kilden.',
    'original_inspired':    'En ny historie med figurer fra norrøn mytologi. Selve handlingen finnes ikke i noen gammel kilde.',
    'original':             'Helt vår egen. Ingen gammel kilde.',
}

NOTEBOLKER = [
    ('kilden',             'Kilden'),
    ('tro_mot_originalen', 'Hva som er tro mot originalen'),
    ('endret',             'Hva som er endret'),
    ('diktet_til',         'Hva som er diktet til'),
    ('om_innholdet',       'Om innholdet'),
    ('videre_lesning',     'Videre lesning'),
]

HODE = """<!DOCTYPE html>
<html lang="nb" data-theme="day">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{tittel} — Pappamål</title>
<meta name="description" content="{beskrivelse}">
<meta name="theme-color" content="#f5f0e8">
<meta property="og:title" content="{ogtittel}">
<meta property="og:description" content="{ogbeskrivelse}">
<meta property="og:type" content="{ogtype}">
<link rel="icon" href="{opp}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400;1,600&family=Lora:ital,wght@0,400;0,600;1,400&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{opp}assets/style.css">
<script>try{{var t=localStorage.getItem('pm:theme');document.documentElement.setAttribute('data-theme',t||(matchMedia('(prefers-color-scheme: dark)').matches?'night':'day'));}}catch(e){{}}</script>
<script src="{opp}assets/app.js" defer></script>
</head>
<body>
"""

FOT = """
<footer class="site-footer">
  <div class="wrap{bred}">
    <div class="rule" role="separator"><span class="diamond"></span></div>
    <p>Pappamål — eventyr fortalt høyt, og skrevet ned etterpå.<br>
    {lenke}</p>
  </div>
</footer>

</body>
</html>
"""


def e(s):
    return html.escape(s or '', quote=True)


def avsnitt(tekst):
    return [p.strip() for p in tekst.split('\n') if p.strip()]


def lesetid(tekst):
    return round(sum(len(p.split()) for p in avsnitt(tekst)) / 95)


def punktliste(verdi):
    """Punkt kan være ren tekst eller {tekst, url}."""
    ut = []
    for x in verdi:
        if isinstance(x, dict):
            ut.append(f'<li><a href="{e(x["url"])}" rel="noopener">{e(x["tekst"])}</a></li>')
        else:
            ut.append(f'<li>{e(x)}</li>')
    return '\n            '.join(ut)


def foreldrenoter(pn):
    bit = []
    for nokkel, tittel in NOTEBOLKER:
        v = pn.get(nokkel)
        if not v:
            continue                      # tom bolk vises ikke
        bit.append(f'          <h3>{tittel}</h3>')
        if isinstance(v, list):
            bit.append('          <ul>\n            ' + punktliste(v) + '\n          </ul>')
        else:
            bit.append(f'          <p>{e(v)}</p>')
    return '\n'.join(bit)


def fortellingsside(s, forrige, neste):
    hylle, aksent = HYLLER[s['shelf']]
    ps = avsnitt(s['story_text'])
    brød = '\n'.join(f'        <p>{e(p)}</p>' for p in ps)
    kilde = KILDEBLOKK[s['source_type']].format(k=e(s.get('source_material') or ''))

    # kildeblokka under navngir verket; pillen sier bare hvor fritt det er gjenfortalt
    piller = [f"{lesetid(s['story_text'])} min høytlesning", KILDETYPE[s['source_type']]]

    def nav(annen, retning, klasse):
        if not annen:
            return (f'        <span class="{klasse} disabled" aria-hidden="true">\n'
                    f'          <span class="dir">{retning}</span>\n'
                    f'          <span class="name">Ingen flere her</span>\n        </span>')
        return (f'        <a class="{klasse}" href="{annen["slug"]}.html" rel="{"prev" if klasse=="prev" else "next"}">\n'
                f'          <span class="dir">{retning}</span>\n'
                f'          <span class="name">{e(annen["title"])}</span>\n        </a>')

    return (
        HODE.format(
            tittel=e(s['title']), opp='../', ogtype='article',
            beskrivelse=e(s.get('teaser') or s.get('summary') or ''),
            ogtittel=e(s['title']), ogbeskrivelse=e(s.get('teaser') or ''))
        + f"""
<div class="wrap">
  <header class="site-header">
    <a class="wordmark" href="../index.html">Pappamål</a>
    <div class="header-tools">
      <div class="text-size" role="group" aria-label="Tekststørrelse">
        <button class="tool-btn" data-size="-" type="button" aria-label="Mindre tekst">A−</button>
        <button class="tool-btn" data-size="+" type="button" aria-label="Større tekst">A+</button>
      </div>
      <button class="tool-btn" data-theme-toggle type="button">☾ Kveld</button>
    </div>
  </header>
</div>

<main>
  <div class="wrap">

    <nav class="breadcrumb" aria-label="Sti">
      <a href="../index.html">Forsiden</a><span class="sep">·</span><a href="../kategorier/{s['shelf']}.html">{hylle}</a>
    </nav>

    <article>
      <header class="story-head" style="--accent: var({aksent})">
        <p class="eyebrow">{hylle}</p>
        <h1>{e(s['title'])}</h1>
        <div class="rule" role="separator"><span class="diamond"></span></div>
        <ul class="meta">
{chr(10).join(f'          <li>{p}</li>' for p in piller)}
        </ul>
      </header>

      <div class="source-block">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
          <circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/>
        </svg>
        <p>{kilde} Se <a href="#foreldre">notene for nysgjerrige foreldre</a> nederst.</p>
      </div>

      <div class="story">
{brød}
        <p class="end" aria-hidden="true">❖</p>
      </div>

      <button class="lest-btn" data-lest="{s['slug']}" type="button" aria-pressed="false">
        <span class="lest-mark" aria-hidden="true"></span>
        <span class="lest-tekst">Marker som lest</span>
      </button>

      <details class="parent-notes" id="foreldre">
        <summary>
          For nysgjerrige foreldre
          <svg class="chev" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>
        </summary>
        <div class="notes-body">

{foreldrenoter(s['parent_notes'])}

        </div>
      </details>

      <nav class="pagenav" aria-label="Bla i hylla">
{nav(forrige, 'Forrige fortelling', 'prev')}
{nav(neste, 'Neste fortelling', 'next')}
      </nav>

    </article>

  </div>
</main>
"""
        + FOT.format(bred='', lenke=f'<a href="../kategorier/{s["shelf"]}.html">Flere fortellinger på denne hylla</a>'))


def kort(s, prefiks):
    piller = [f"{s['lesetid']} min høytlesning", KILDETYPE[s['source_type']]]
    return f"""      <li>
        <a class="story-card" href="{prefiks}{s['slug']}.html" data-slug="{s['slug']}">
          <h3>{e(s['title'])}</h3>
          <p class="teaser">{e(s['teaser'])}</p>
          <span class="source">{e(s['kildelinje'])}</span>
          <ul class="meta">
{chr(10).join(f'            <li>{p}</li>' for p in piller)}
          </ul>
        </a>
      </li>"""


# --- manifest: de to håndskrevne + de seks genererte ------------------------

HANDSKREVNE = [
    dict(slug='odin-og-vavtrudne', title='Odin og jotnen som kunne alle svarene',
         teaser='Den klokeste jotnen i Jotunheim møter en vandrer som stiller ett spørsmål for mye.',
         kildelinje='Fritt etter Vavtrudnesmål, Den eldre Edda', lesetid=6,
         source_type='authentic_adaptation', shelf='norrone', generert=False),
    dict(slug='tor-og-alvis', title='Tor og dvergen som visste alt',
         teaser='En dverg banker på og krever å få gifte seg. Tor griper ikke hammeren — han stiller spørsmål.',
         kildelinje='Fritt etter Alvismål, Den eldre Edda', lesetid=5,
         source_type='authentic_adaptation', shelf='norrone', generert=False),
]

# Leserekkefølge, satt etter hva som skjer først, ikke etter når det ble skrevet.
# De to håndskrevne står først, fordi bygg.py bare kan rette neste-lenken deres.
# Ellers: muren før alt annet (Åsgard får muren og Odin får hesten), dvergegavene
# før Tor-fortellingene (Mjølner blir til der), Idun før Skade (Tjatse er faren
# hennes), leirmannen før tåa (Tor får steinen i hodet, og Groa synger etterpå),
# fjærdrakten før den farlige elva (Loke blir tatt der og lover Tor bort).
REKKEFOLGE = ['odin-og-vavtrudne', 'tor-og-alvis',
              'muren-rundt-asgard', 'odin-og-mimes-bronn',
              'odin-og-den-magiske-dikterdrikken', 'loke-og-dvergegavene',
              'tyr-og-fenrir', 'idun-og-eplene', 'skade-og-de-vakreste-fottene',
              'tor-og-leirmannen', 'tor-og-taa-som-ble-en-stjerne',
              'loke-og-froyas-fjaerdrakt', 'tor-og-den-farlige-elva',
              'tor-i-brudeklaer', 'tor-hos-utgard-loke', 'balder-og-misteltein',
              # Antikken: ilden først, og krukken rett etter — den er Zevs' svar på den.
              'prometevs-og-ilden', 'pandora-og-krukken', 'persefone-og-kjernen',
              'arakne-og-veven', 'kong-midas', 'psyke-og-oppgavene',
              'odyssevs-og-kyklopen', 'dedalus-og-ikaros']


def last():
    """Alle .json-filer i data/ er kilder. Rekkefølgen bestemmes av REKKEFOLGE."""
    alle = {x['slug']: x for x in HANDSKREVNE}
    katalog = os.path.join(ROT, 'data')
    for navn in sorted(os.listdir(katalog)):
        if not navn.endswith('.json'):
            continue
        d = json.load(open(os.path.join(katalog, navn), encoding='utf-8'))
        for s in d['stories']:
            s = dict(s, generert=True, lesetid=lesetid(s['story_text']),
                     kildelinje=('Fritt etter ' + s['source_material'] if s.get('source_material')
                                 else 'Ny historie med gamle figurer'))
            # Fjærdrakten står på Hjemmelagede i eksporten, men har Frøy, Frøya og Loke,
            # og noter som viser til kilder. Hylla lover "ingen kilde å vise til".
            if s['slug'] == 'loke-og-froyas-fjaerdrakt':
                s['shelf'] = 'norrone'
            alle[s['slug']] = s
    mangler = [k for k in alle if k not in REKKEFOLGE]
    if mangler:
        raise SystemExit('mangler i REKKEFOLGE: ' + ', '.join(sorted(mangler)))
    return [alle[k] for k in REKKEFOLGE if k in alle]


def main():
    alle = last()
    skrevet = []

    for hylle in HYLLER:
        ihylle = [s for s in alle if s['shelf'] == hylle]
        for i, s in enumerate(ihylle):
            if not s.get('generert'):
                continue
            f = os.path.join(ROT, 'fortellinger', s['slug'] + '.html')
            open(f, 'w', encoding='utf-8').write(
                fortellingsside(s, ihylle[i - 1] if i else None,
                                ihylle[i + 1] if i + 1 < len(ihylle) else None))
            skrevet.append(f)

    # forrige/neste i de to håndskrevne — bare navigasjonen, aldri teksten
    for i, s in enumerate([x for x in alle if x['shelf'] == 'norrone']):
        if s.get('generert'):
            continue
        ihylle = [x for x in alle if x['shelf'] == 'norrone']
        nxt = ihylle[i + 1] if i + 1 < len(ihylle) else None
        f = os.path.join(ROT, 'fortellinger', s['slug'] + '.html')
        h = open(f, encoding='utf-8').read()
        nyt = (f'<a class="next" href="{nxt["slug"]}.html" rel="next">\n'
               f'          <span class="dir">Neste fortelling</span>\n'
               f'          <span class="name">{e(nxt["title"])}</span>\n        </a>')
        h = re.sub(r'<(a|span) class="next[^"]*"[^>]*>.*?</\1>', nyt, h, flags=re.S)
        open(f, 'w', encoding='utf-8').write(h)
        skrevet.append(f + ' (bare navigasjon)')

    # hyllesider — behold "bare fortalt"-kortene som alt står der
    for hylle, (navn, aksent) in HYLLER.items():
        ihylle = [s for s in alle if s['shelf'] == hylle]
        if not ihylle:
            continue                      # tom hylle beholder kortene sine urørt
        f = os.path.join(ROT, 'kategorier', hylle + '.html')
        h = open(f, encoding='utf-8').read()
        ferdige = '\n'.join(kort(s, '../fortellinger/') for s in ihylle)
        m = re.search(r'(<ul class="story-list">\n)(.*?)(\n      <li>\n        <div class="story-card story-card--soon">)',
                      h, flags=re.S)
        if m:
            h = h[:m.start(2)] + ferdige + h[m.end(2):]
        elif ferdige:
            h = re.sub(r'<p class="empty-note">.*?</p>',
                       f'<ul class="story-list">\n{ferdige}\n    </ul>', h, flags=re.S)
            h = re.sub(r'<ul class="story-list">\n\s*</ul>', f'<ul class="story-list">\n{ferdige}\n    </ul>', h)
        open(f, 'w', encoding='utf-8').write(h)
        skrevet.append(f)

    # forsiden: fortellingslista og telleverkene
    f = os.path.join(ROT, 'index.html')
    h = open(f, encoding='utf-8').read()
    lista = '\n'.join(kort(s, 'fortellinger/') for s in alle)
    h = re.sub(r'(<ul class="story-list">\n).*?(\n    </ul>)', r'\1' + lista.replace('\\', '\\\\') + r'\2',
               h, flags=re.S)
    for hylle, (navn, _) in HYLLER.items():
        n = len([s for s in alle if s['shelf'] == hylle])
        sti = os.path.join(ROT, 'kategorier', hylle + '.html')
        soon = open(sti, encoding='utf-8').read().count('story-card--soon')
        bit = []
        if n:
            bit.append(f'{n} skrevet ned')
        if soon:
            bit.append(f'{soon} fortalt')
        h = re.sub(rf'(href="kategorier/{hylle}\.html".*?<span class="count">)[^<]*(</span>)',
                   lambda m, t=' · '.join(bit) or 'Ingen ennå': m.group(1) + t + m.group(2),
                   h, flags=re.S)
    open(f, 'w', encoding='utf-8').write(h)
    skrevet.append(f)

    for x in skrevet:
        print('skrev', os.path.relpath(x, ROT) if not x.endswith(')') else os.path.relpath(x.split(' (')[0], ROT) + ' (nav)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
