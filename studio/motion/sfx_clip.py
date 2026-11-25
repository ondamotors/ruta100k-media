#!/usr/bin/env python3
"""Bruitages du reel CLIP (compteur de vues qui monte jusqu'à 1M). Synthèse pure.
  python sfx_clip.py out.wav 11.85
"""
import sys, wave
import numpy as np
from sfx_gratis import SR, whoosh, ding, boom
from sfx_burger import pop, click

T0, T1 = 1.45, 4.45
B = T1
SH = B + 1.85
K = SH + 2.25

def main(dest, dur):
    out = np.zeros(int(SR * (dur + 2)))
    def add(sig, t0, g):
        i = int(t0 * SR); out[i:i + len(sig)] += sig * g
    for i in range(3):
        add(pop(1200, 800, d=0.07), 0.35 + i * 0.18, 0.12)
    t, gap, k = T0, 0.13, 0
    while t < T1 - 0.02:                                    # le compteur qui s'emballe
        add(click(300 + k, d=0.015), t, 0.09); t += gap; gap = max(0.028, gap * 0.93); k += 1
    for m, f in ((10000, 1567.98), (100000, 1975.53)):
        add(ding(f, d=0.6), T0 + (m / 1e6) ** (1 / 3) * (T1 - T0), 0.22)
    add(boom(), B, 0.75)
    for f in (1318.51, 1661.22, 1975.53, 2637.02):
        add(ding(f, d=1.4), B + 0.02, 0.16)
    add(pop(), B + 0.15, 0.13); add(pop(), B + 0.4, 0.13)
    add(whoosh(d=0.34, seed=61, lo=400, hi=3500), SH - 0.02, 0.16)
    for i in range(3):
        add(pop(1100, 700, d=0.08), SH + 0.35 + i * 0.3, 0.12)
    add(whoosh(d=0.3, seed=62, lo=400, hi=3000), K - 0.08, 0.14)
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
