#!/usr/bin/env python3
"""Bruitages du reel PAGO (TikTok paie ? selon le pays). Synthèse pure.
  python sfx_pago.py out.wav 9.85
"""
import sys, wave
import numpy as np
import scipy.signal as sg
from sfx_gratis import SR, whoosh, ding, boom
from sfx_burger import pop, click

C = [0.35, 1.05, 1.65, 2.20, 2.70, 3.15]
NAMES = ['México', 'Colombia', 'Argentina', 'Brasil', 'Chile', 'Perú']
OK = [True, False, False, True, False, False]
TYPE = 0.24
SH = 4.35
K = 6.55

def buzz(d=0.26, f=155.56):
    n = int(SR * d); t = np.arange(n) / SR
    s = sum((1 / k) * (np.sin(2 * np.pi * f * k * t) + np.sin(2 * np.pi * f * 1.015 * k * t)) for k in (1, 3, 5, 7))
    env = np.minimum(1, t / 0.004) * np.where(t > d - 0.08, np.exp(-(t - (d - 0.08)) / 0.03), 1)
    b, a = sg.butter(2, 3000 / (SR / 2))
    s = sg.lfilter(b, a, s * env)
    return s / np.max(np.abs(s))

def main(dest, dur):
    out = np.zeros(int(SR * (dur + 2)))
    def add(sig, t0, g):
        i = int(t0 * SR); out[i:i + len(sig)] += sig * g
    for i, c in enumerate(C):
        n = len(NAMES[i])
        for j in range(n):
            add(click(100 + i * 20 + j, d=0.02), c + j * TYPE / n, 0.10)
        r = c + TYPE + 0.11
        if OK[i]:
            add(ding(1318.51 if i == 0 else 1975.53, d=0.8), r, 0.30)
            add(ding(1661.22 if i == 0 else 2489.02, d=0.8), r + 0.06, 0.16)
        else:
            add(buzz(), r, 0.20)
    add(pop(), 3.62, 0.16)
    add(whoosh(d=0.34, seed=31, lo=400, hi=3500), SH - 0.02, 0.16)
    for k in range(4):
        add(pop(1300, 800, d=0.07), SH + 0.32 + k * 0.2, 0.13)
    add(whoosh(d=0.3, seed=32, lo=400, hi=3000), K - 0.08, 0.14)
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
