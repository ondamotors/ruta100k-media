#!/usr/bin/env python3
"""Bruitages du reel AUTO (l'IA programme et publie). Synthèse pure.
  python sfx_auto.py out.wav 12.9
"""
import sys, wave
import numpy as np
from sfx_gratis import SR, whoosh, ding, boom
from sfx_burger import pop, click
from sfx_clave import ping

TYPE0, TYPE1 = 0.45, 1.05
N = 3.3
MO = 5.05
SHOP = [MO + 0.55, MO + 0.8, MO + 1.02, MO + 1.22, MO + 1.4]
B = MO + 1.65
SH = B + 1.9
K = SH + 2.3

def main(dest, dur):
    out = np.zeros(int(SR * (dur + 2)))
    def add(sig, t0, g):
        i = int(t0 * SR); out[i:i + len(sig)] += sig * g
    k = 0
    for tt in np.linspace(TYPE0, TYPE1 - 0.03, 14):
        add(click(400 + k, d=0.02), tt, 0.09); k += 1
    add(whoosh(d=0.14, seed=81, lo=1500, hi=7000), TYPE1 + 0.02, 0.12)
    add(pop(1100, 700), TYPE1 + 0.1, 0.12)
    add(ping(), 1.6, 0.18)
    for i in range(21):
        add(pop(900 + 40 * i, 600 + 30 * i, d=0.05), 1.9 + i * 0.055, 0.07)
    add(ding(2637.02, d=0.6), 1.9 + 21 * 0.055, 0.18)
    add(whoosh(d=0.3, seed=82, lo=300, hi=2500), N - 0.05, 0.14)
    for j in range(3):
        add(ping(), N + 0.3 + j * 0.35, 0.16)
    add(whoosh(d=0.34, seed=83, lo=400, hi=3500), MO - 0.02, 0.16)
    notes = [1318.51, 1567.98, 1760.0, 2093.0, 2637.02]
    for i, t in enumerate(SHOP):
        add(ding(notes[i], d=0.45), t + 0.05, 0.2)
    add(boom(), B, 0.75)
    for f in (1318.51, 1661.22, 1975.53, 2637.02):
        add(ding(f, d=1.4), B + 0.02, 0.16)
    add(pop(), B + 0.1, 0.13); add(pop(), B + 0.3, 0.13)
    add(whoosh(d=0.34, seed=84, lo=400, hi=3500), SH - 0.02, 0.16)
    for i in range(3):
        add(pop(1100, 700, d=0.08), SH + 0.35 + i * 0.32, 0.12)
    add(whoosh(d=0.3, seed=85, lo=400, hi=3000), K - 0.08, 0.14)
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
