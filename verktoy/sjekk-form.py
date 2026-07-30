#!/usr/bin/env python3
"""Mål en fortelling mot formen i FORTELLERFORM.md.

    python3 verktoy/sjekk-form.py < fortelling.txt

Leser del A — bare fortellingen, én linje per avsnitt, ingen overskrift og ingen metadata.

Skiller mellom STEMME og STØRRELSE:

  Stemmen er forhold, ikke tall. En lang fortelling og en kort fortelling skal ha samme
  replikkandel og samme avsnittsrytme. Disse er harde krav, og de avgjør exit-koden.

  Størrelsen er fri. En fortelling med fire figurer som hver skal ha en tråd, trenger mer
  plass enn en med to. Lengden rapporteres som en klasse, ikke som en feil.

Tersklene er kalibrert på fortellingene i fortellinger/, som passerer alle stemmekravene.
"""

import re
import statistics as st
import sys

KLASSER = [
    ('kort',    0,   550),
    ('middels', 550, 750),
    ('lang',    750, 1000),
    ('svært lang', 1000, 10 ** 9),
]


def klasse(ord_):
    for navn, lo, hi in KLASSER:
        if lo <= ord_ < hi:
            return navn
    return 'ukjent'


def main() -> int:
    ps = [l.strip() for l in sys.stdin.read().split('\n') if l.strip()]
    if not ps:
        print('FEIL  tom tekst')
        return 1

    w = [len(p.split()) for p in ps]
    n = len(ps)
    ord_ = sum(w)
    replikker = sum(1 for p in ps if p.startswith('–'))
    en_setning = sum(1 for p in ps if len(re.findall(r'[.!?](?:\s|$)', p)) == 1)
    korte = sum(1 for x in w if x <= 8)
    lange_pr100 = sum(1 for x in w if x > 25) / n * 100
    utrop_pr100 = ' '.join(ps).count('!') / n * 100

    # Stemmen — forhold. Harde krav.
    stemme = [
        ('median 5-7 ord',        5 <= st.median(w) <= 7,            st.median(w)),
        ('>=70% under 9 ord',     korte / n >= .70,                  f'{100 * korte // n}%'),
        ('>=75% en setning',      en_setning / n >= .75,             f'{100 * en_setning // n}%'),
        ('replikker 40-55%',      .40 <= replikker / n <= .55,       f'{100 * replikker // n}%'),
        ('ingen over 35 ord',     max(w) <= 35,                      max(w)),
        ('<=2 lange pr 100 avsn', lange_pr100 <= 2.0,                f'{lange_pr100:.1f}'),
        ('<=6 utrop pr 100 avsn', utrop_pr100 <= 6.0,                f'{utrop_pr100:.1f}'),
    ]

    print('STEMME — harde krav')
    for navn, ok, verdi in stemme:
        print(f"  {'OK  ' if ok else 'FEIL'}  {navn:24} {verdi}")

    print(f'\nSTØRRELSE — fri, oppgis ikke som feil')
    print(f'  {ord_} ord i {n} avsnitt — {klasse(ord_)}')
    print(f'  lesetid: {round(ord_ / 95)} min')

    feil = [navn for navn, ok, _ in stemme if not ok]
    if feil:
        mangler = max(0, round(.40 * n) - replikker)
        print(f'\n{len(feil)} stemmekrav ryker: {", ".join(feil)}')
        if mangler:
            print(f'{mangler} fortellersetninger må bli replikk for å nå 40 %.')
        return 1

    print('\nLes etter: den doble moralen, den flate tonen, tre runder i slag 5.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
