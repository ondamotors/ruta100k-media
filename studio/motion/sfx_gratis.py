#!/usr/bin/env python3
"""Bruitages du reel GRATIS, synthétisés (aucun échantillon externe).
Swipe = souffle filtré, chaque baisse du compteur = note de glockenspiel qui monte, $0 = impact + accord.
  python sfx_gratis.py out.wav 9.6667
"""
import sys, wave
import numpy as np
import scipy.signal as sg

SR = 44100
S = [0.40, 1.15, 1.85, 2.50, 3.10, 3.65]
B = 4.62
K = B + 2.0
NOTES = [1318.51, 1479.98, 1661.22, 1975.53, 2217.46, 2637.02]  # mi6 fa#6 sol#6 si6 do#7 mi7

def whoosh(d=0.26, seed=1, lo=700, hi=5200):
    n = int(SR * d)
    x = np.random.default_rng(seed).standard_normal(n)
    b, a = sg.butter(2, [lo / (SR / 2), hi / (SR / 2)], btype='band')
    x = sg.lfilter(b, a, x)
    t = np.linspace(0, 1, n)
    env = np.sin(np.pi * t ** 0.65) ** 2
    x = x * env
    return x / np.max(np.abs(x))

def ding(f, d=0.75):
    n = int(SR * d)
    t = np.arange(n) / SR
    parts = [(1.0, 1.0, 0.50), (2.0, 0.18, 0.28), (2.76, 0.30, 0.20), (5.40, 0.10, 0.08)]
    s = sum(a * np.sin(2 * np.pi * f * r * t) * np.exp(-t / dec) for r, a, dec in parts)
    s *= np.minimum(1, t / 0.002)
    click = np.random.default_rng(int(f)).standard_normal(n) * np.exp(-t / 0.004) * 0.25
    s = s + click
    return s / np.max(np.abs(s))

def boom(d=1.0):
    n = int(SR * d)
    t = np.arange(n) / SR
    f = 42 + 70 * np.exp(-t / 0.10)
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.38)
    nz = np.random.default_rng(2).standard_normal(n)
    b, a = sg.butter(2, 350 / (SR / 2))
    nz = sg.lfilter(b, a, nz) * np.exp(-t / 0.07)
    s = s + 0.7 * nz / np.max(np.abs(nz))
    return s / np.max(np.abs(s))

def main(dest, dur):
    out = np.zeros(int(SR * (dur + 1.5)))
    def add(sig, t0, g):
        i = int(t0 * SR)
        out[i:i + len(sig)] += sig * g
    for i, s in enumerate(S):
        add(whoosh(seed=10 + i), s, 0.16)
        add(ding(NOTES[i]), s + 0.62, 0.30)
    add(boom(), B, 0.75)
    for f in [1318.51, 1661.22, 1975.53, 2637.02]:
        add(ding(f, d=1.4), B + 0.02, 0.16)
    add(whoosh(d=0.34, seed=99, lo=400, hi=3000), K - 0.08, 0.14)
    add(ding(1975.53, d=0.5), K + 0.5, 0.14)
    out = out[:int(SR * dur)]
    fade = int(SR * 0.05)
    out[-fade:] *= np.linspace(1, 0, fade)
    out = out / np.max(np.abs(out)) * 0.70
    pcm = (out * 32767).astype(np.int16)
    st = np.repeat(pcm[:, None], 2, axis=1)
    with wave.open(dest, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(st.tobytes())
    print('OK', dest, f'{dur:.2f} s', 'peak', round(float(np.max(np.abs(out))), 2))

if __name__ == '__main__':
    main(sys.argv[1], float(sys.argv[2]))
