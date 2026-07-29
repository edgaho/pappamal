#!/usr/bin/env python3
"""Mål en fortelling mot formen i FORTELLERFORM.md.

    python3 verktoy/sjekk-form.py < fortelling.txt

Leser del A — bare fortellingen, én linje per avsnitt, ingen overskrift og ingen metadata.
Tersklene er kalibrert slik at begge fortellingene i fortellinger/ passerer alle ni.
Avslutter med kode 1 hvis noe feiler, så den kan brukes som gate i et skript.
"""

import re
import statistics as st
import sys


def main() -> int:
    ps = [l.strip() for l in sys.stdin.read().split('\n') if l.strip()]
    if not ps:
        print('FEIL  tom tekst')
        return 1

    w = [len(p.split()) for p in ps]
    replikker = sum(1 for p in ps if p.startswith('–'))
    en_setning = sum(1 for p in ps if len(re.findall(r'[.!?](?:\s|$)', p)) == 1)
    korte = sum(1 for x in w if x <= 8)
    lange = sum(1 for x in w if x > 25)
    utrop = ' '.join(ps).count('!')

    sjekk = [
        ('avsnitt 50-85',       50 <= len(ps) <= 85,               len(ps)),
        ('ord 450-650',         450 <= sum(w) <= 650,              sum(w)),
        ('median 5-7 ord',      5 <= st.median(w) <= 7,            st.median(w)),
        ('>=70% under 9 ord',   korte / len(w) >= .70,             f'{100 * korte // len(w)}%'),
        ('<=1 avsnitt over 25', lange <= 1,                        lange),
        ('ingen over 35 ord',   max(w) <= 35,                      max(w)),
        ('>=75% en setning',    en_setning / len(ps) >= .75,       f'{100 * en_setning // len(ps)}%'),
        ('replikker 40-55%',    .40 <= replikker / len(ps) <= .55, f'{100 * replikker // len(ps)}%'),
        ('<=3 utropstegn',      utrop <= 3,                        utrop),
    ]

    for navn, ok, verdi in sjekk:
        print(f"{'OK  ' if ok else 'FEIL'}  {navn:22} {verdi}")

    print('lesetid:', round(sum(w) / 95), 'min')

    # Det som ikke kan måles må leses — minn om hva.
    if all(ok for _, ok, _ in sjekk):
        print('\nLes etter: den doble moralen, den flate tonen, tre runder i slag 5.')

    return 0 if all(ok for _, ok, _ in sjekk) else 1


if __name__ == '__main__':
    sys.exit(main())
