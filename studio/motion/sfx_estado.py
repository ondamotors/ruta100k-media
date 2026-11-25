#!/usr/bin/env python3
"""Bruitages du reel ESTADO (Account check). Synthèse pure.
  python sfx_estado.py out.wav 10.54
"""
import sys, wave
import numpy as np
from sfx_gratis import SR, whoosh, ding, boom
from sfx_burger import pop, click
from sfx_pago import buzz
from sfx_clave import alarm, thump

SW, S0, STEP, N = 1.0, 1.4, 0.27, 7
HL = S0 + N * STEP + 0.15
SH = HL + 1.6
K = SH + 2.2
NOTES = [1046.5, 1174.66, 1318.51, 1396.91, 1567.98, 1760.0, 1975.53]

def main(dest, dur):
    out = np.zeros(int(SR * (dur + 2)))
    def add(sig, t0, g):
        i = int(t0 * SR); out[i:i + len(sig)] += sig * g
    add(pop(1100, 700), 0.5, 0.12)
    add(click(9), 0.84, 0.3)
    add(whoosh(d=0.3, seed=51), SW, 0.15)
    for i in range(N):
        add(ding(NOTES[i], d=0.35), S0 + (i + 1) * STEP, 0.12)
    add(alarm(), HL, 0.16)
    add(thump(), HL, 0.55)
    add(ding(2637.02, d=0.8), HL + 0.02, 0.2)
    add(pop(), HL + 0.1, 0.13); add(pop(), HL + 0.35, 0.13)
    add(whoosh(d=0.34, seed=52, lo=400, hi=3500), SH - 0.02, 0.16)
    for k in range(3):
        add(buzz(d=0.18), SH + 0.35 + k * 0.3, 0.1)
    add(whoosh(d=0.3, seed=53, lo=400, hi=3000), K - 0.08, 0.14)
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
