#!/usr/bin/env python3
"""Bruitages du reel UGC (10 prises, compteur qui monte). Synthèse pure.
  python sfx_ugc.py out.wav 11.65
"""
import sys, wave
import numpy as np
import scipy.signal as sg
from sfx_gratis import SR, whoosh, ding, boom
from sfx_burger import pop

TAKES = [0.55, 1.15, 1.65, 2.08, 2.46, 2.8, 3.1, 3.36, 3.59, 3.8]
B = 4.25
SH = B + 1.8
K = SH + 2.3
NOTES = [1046.5, 1174.66, 1318.51, 1567.98, 1760.0, 2093.0, 2349.32, 2637.02, 3135.96, 3520.0]

def shutter(seed=1):
    n = int(SR * 0.09); t = np.arange(n) / SR
    rng = np.random.default_rng(seed)
    x = rng.standard_normal(n)
    b, a = sg.butter(2, [1500 / (SR / 2), 8000 / (SR / 2)], btype='band')
    x = sg.lfilter(b, a, x)
    env = np.exp(-t / 0.006) + 0.8 * np.exp(-np.clip(t - 0.035, 0, None) / 0.008) * (t >= 0.035)
    s = x * env
    return s / np.max(np.abs(s))

def main(dest, dur):
    out = np.zeros(int(SR * (dur + 2)))
    def add(sig, t0, g):
        i = int(t0 * SR); out[i:i + len(sig)] += sig * g
    for i, t in enumerate(TAKES):
        add(shutter(i), t, 0.3)
        add(ding(NOTES[i], d=0.45), t + 0.38, 0.17)
    add(boom(), B, 0.75)
    for f in (1318.51, 1661.22, 1975.53, 2637.02):
        add(ding(f, d=1.4), B + 0.02, 0.16)
    add(pop(), B + 0.1, 0.13); add(pop(), B + 0.3, 0.13)
    add(whoosh(d=0.34, seed=71, lo=400, hi=3500), SH - 0.02, 0.16)
    for k in range(3):
        add(pop(1100, 700, d=0.08), SH + 0.35 + k * 0.32, 0.12)
    add(ding(2637.02, d=0.7), SH + 1.1, 0.16)
    add(whoosh(d=0.3, seed=72, lo=400, hi=3000), K - 0.08, 0.14)
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
