#!/usr/bin/env python3
"""Bruitages du reel ENTRENA (payé en dollars pour corriger l'espagnol de l'IA). Synthèse pure.
  python sfx_entrena.py out.wav 12.7
"""
import sys, wave
import numpy as np
from sfx_gratis import SR, whoosh, ding, boom
from sfx_burger import pop, click
from sfx_clave import ping, thump
from sfx_pago import buzz

T = [
    dict(a=0.35, x=0.85, c0=1.0, c1=1.35, s=1.42),
    dict(a=1.88, x=2.12, c0=2.22, c1=2.48, s=2.53),
    dict(a=2.93, x=3.15, c0=3.25, c1=3.5, s=3.55),
]
SW = [1.7, 2.75]
G = 1.62
MO = 3.9
ROWT = [MO + 0.35, MO + 0.6]
PAGO = MO + 0.85
C0, B = MO + 1.1, MO + 1.9
SH = B + 1.8
K = SH + 2.1


def main(dest, dur):
    out = np.zeros(int(SR * (dur + 2)))

    def add(sig, t0, g):
        i = int(t0 * SR); out[i:i + len(sig)] += sig * g

    add(whoosh(d=0.25, seed=101, lo=500, hi=4500), 0.0, 0.13)
    add(pop(1200, 700), 0.04, 0.12)
    k = 0
    notes = [1318.51, 1567.98, 1975.53]
    for i, t in enumerate(T):
        add(ping(), t['a'], 0.14)
        add(click(1100 + i, d=0.03), t['x'] - 0.04, 0.15)
        add(buzz(d=0.16), t['x'], 0.1)
        for tt in np.linspace(t['c0'], t['c1'] - 0.03, 8):
            add(click(1200 + k, d=0.02), tt, 0.08); k += 1
        add(ding(notes[i], d=0.55), t['s'], 0.2)
        add(pop(1100, 700), t['s'], 0.1)
    for t in SW:
        add(whoosh(d=0.2, seed=102 + int(t * 10), lo=800, hi=5000), t, 0.12)
    add(pop(), G, 0.12); add(pop(), G + 0.16, 0.12)
    add(whoosh(d=0.34, seed=103, lo=400, hi=3500), MO - 0.02, 0.16)
    for t in ROWT:
        add(pop(1000, 650, d=0.08), t, 0.12)
    add(pop(1000, 650, d=0.08), PAGO, 0.11)
    # compteur qui accélère
    ts = C0 + (B - C0) * np.sqrt(np.linspace(0, 1, 16))[:-1]
    for tt in ts:
        add(click(1300 + k, d=0.015), tt, 0.07); k += 1
    add(boom(), B, 0.75)
    for f in (1318.51, 1661.22, 1975.53, 2637.02):
        add(ding(f, d=1.4), B + 0.02, 0.16)
    add(pop(), B + 0.05, 0.12); add(pop(), B + 0.18, 0.13); add(pop(), B + 0.42, 0.12)
    add(thump(), B + 0.3, 0.22)
    add(whoosh(d=0.34, seed=104, lo=400, hi=3500), SH - 0.02, 0.16)
    add(pop(), SH + 0.12, 0.11); add(pop(), SH + 0.3, 0.11)
    for i in range(3):
        add(pop(1100, 700, d=0.08), SH + 0.35 + i * 0.3, 0.12)
    add(whoosh(d=0.3, seed=105, lo=400, hi=3000), K - 0.08, 0.14)
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
