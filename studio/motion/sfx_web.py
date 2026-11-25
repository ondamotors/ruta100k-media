#!/usr/bin/env python3
"""Bruitages du reel WEB (webs faites avec l'IA pour les commerces sans site). Synthèse pure.
  python sfx_web.py out.wav 13.3
"""
import sys, wave
import numpy as np
from sfx_gratis import SR, whoosh, ding, boom
from sfx_burger import pop, click
from sfx_clave import ping, thump

SQ0, SQ1 = 0.12, 0.6
ROWS = [0.62, 0.7, 0.78, 0.86]
STAMP = [1.0, 1.18, 1.36]
G = 1.3
CH = 2.25
TYPE0, TYPE1 = CH + 0.2, CH + 0.7
BLD = [3.48, 3.62, 3.78, 3.94, 4.1]
LK = 4.4
MO = 4.85
SHOP = [MO + 0.8 + i * 0.075 for i in range(10)]
B = MO + 1.6
SH = B + 1.75
K = SH + 2.1


def main(dest, dur):
    out = np.zeros(int(SR * (dur + 2)))

    def add(sig, t0, g):
        i = int(t0 * SR); out[i:i + len(sig)] += sig * g

    # accroche
    add(whoosh(d=0.25, seed=91, lo=500, hi=4500), 0.0, 0.13)
    add(pop(1200, 700), 0.04, 0.12)
    k = 0
    for tt in np.linspace(SQ0, SQ1 - 0.03, 12):
        add(click(500 + k, d=0.02), tt, 0.08); k += 1
    for i, t in enumerate(ROWS):
        add(pop(900 + 90 * i, 600 + 60 * i, d=0.06), t + 0.04, 0.1)
    for i, t in enumerate(STAMP):
        add(thump(), t, 0.4)
        add(click(700 + i, d=0.03), t, 0.14)
    add(pop(), G, 0.12); add(pop(), G + 0.16, 0.12)
    # on tape, la IA fait la web
    add(click(801, d=0.03), CH - 0.2, 0.16)
    add(whoosh(d=0.3, seed=92, lo=400, hi=3500), CH, 0.16)
    add(pop(), CH + 0.12, 0.12); add(pop(), CH + 0.28, 0.12)
    for tt in np.linspace(TYPE0, TYPE1 - 0.03, 14):
        add(click(900 + k, d=0.02), tt, 0.09); k += 1
    add(whoosh(d=0.14, seed=93, lo=1500, hi=7000), TYPE1 + 0.02, 0.12)
    add(pop(1100, 700), TYPE1 + 0.1, 0.12)
    add(ping(), 3.3, 0.18)
    add(whoosh(d=0.18, seed=94, lo=900, hi=6000), 3.42, 0.08)
    for i, t in enumerate(BLD):
        add(pop(1000 + 140 * i, 700 + 100 * i, d=0.06), t, 0.11)
    add(ding(2637.02, d=0.6), LK, 0.2)
    add(ping(), LK + 0.05, 0.12)
    # l'argent
    add(whoosh(d=0.34, seed=95, lo=400, hi=3500), MO - 0.02, 0.16)
    for tt in np.linspace(MO + 0.3, MO + 0.72, 9):
        add(click(1000 + k, d=0.015), tt, 0.06); k += 1
    add(ding(1567.98, d=0.5), MO + 0.75, 0.16)
    notes = [1046.5, 1174.66, 1318.51, 1396.91, 1567.98, 1760.0, 1975.53, 2093.0, 2349.32, 2637.02]
    for i, t in enumerate(SHOP):
        add(ding(notes[i], d=0.3), t + 0.02, 0.12)
    add(boom(), B, 0.75)
    for f in (1318.51, 1661.22, 1975.53, 2637.02):
        add(ding(f, d=1.4), B + 0.02, 0.16)
    add(pop(), B + 0.1, 0.13); add(pop(), B + 0.3, 0.13)
    # les étapes
    add(whoosh(d=0.34, seed=96, lo=400, hi=3500), SH - 0.02, 0.16)
    add(pop(), SH + 0.12, 0.11); add(pop(), SH + 0.3, 0.11)
    for i in range(3):
        add(pop(1100, 700, d=0.08), SH + 0.35 + i * 0.3, 0.12)
    # commente
    add(whoosh(d=0.3, seed=97, lo=400, hi=3000), K - 0.08, 0.14)
    add(boom(), K, 0.35)
    add(pop(), K + 0.06, 0.13); add(pop(), K + 0.3, 0.13)
    add(ding(1975.53, d=0.7), K + 0.5, 0.22)
    add(pop(1000, 560), K + 0.85, 0.11); add(pop(1000, 560), K + 1.05, 0.1)

    out = out[:int(SR * dur)]
    fade = int(SR * 0.06); out[-fade:] *= np.linspace(1, 0, fade)
    out = out / np.max(np.abs(out)) * 0.70
    pcm = (out * 32767).astype(np.int16)
    with wave.open(dest, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(np.repeat(pcm[:, None], 2, axis=1).tobytes())
    print('OK', dest, f'{dur:.2f} s')


if __name__ == '__main__':
    main(sys.argv[1], float(sys.argv[2]))
