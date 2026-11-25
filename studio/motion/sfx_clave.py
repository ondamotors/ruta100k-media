#!/usr/bin/env python3
"""Bruitages du reel CLAVE (voix clonée). Synthèse pure : la note vocale est un marmonnement
synthétique (formants), volontairement inintelligible et un peu robotique.
  python sfx_clave.py out.wav 11.75
"""
import sys, wave
import numpy as np
import scipy.signal as sg
from sfx_gratis import SR, whoosh, ding, boom
from sfx_burger import pop, click

PLAY0, PLAY1 = 0.62, 2.45
R = 2.55
TYPE0, TYPE1 = 4.35, 4.9
TY, TYEND = 5.25, 6.45
K = 8.45

def ping():
    n = int(SR * 0.22); t = np.arange(n) / SR
    s = np.sin(2 * np.pi * 1046.5 * t) * np.exp(-t / 0.05) * (t < 0.08)
    t2 = np.clip(t - 0.07, 0, None)
    s = s + np.sin(2 * np.pi * 1568.0 * t2) * np.exp(-t2 / 0.07) * (t >= 0.07)
    return s / np.max(np.abs(s))

def babble(d, seed=3):
    rng = np.random.default_rng(seed)
    n = int(SR * d); t = np.arange(n) / SR
    f0 = 128 + 18 * np.sin(2 * np.pi * 1.1 * t) + 9 * np.sin(2 * np.pi * 2.7 * t)
    ph = 2 * np.pi * np.cumsum(f0) / SR
    src = sum(np.sin(k * ph) / k for k in range(1, 28))
    vowels = [(800, 1200), (500, 1900), (300, 2300), (500, 900), (350, 800), (700, 1700)]
    out = np.zeros(n); i = 0
    while i < n:
        seg = int(SR * rng.uniform(0.09, 0.17))
        j = min(n, i + seg)
        f1, f2 = vowels[rng.integers(len(vowels))]
        x = src[i:j]
        y = np.zeros_like(x)
        for f, g in ((f1, 1.0), (f2, 0.6)):
            b, a = sg.iirpeak(f / (SR / 2), Q=6)
            y += g * sg.lfilter(b, a, x)
        m = j - i; tt = np.arange(m) / SR
        env = np.minimum(1, tt / 0.02) * np.exp(-tt / 0.12)
        if rng.random() < 0.45:
            nz = rng.standard_normal(m) * np.exp(-tt / 0.012) * 0.6
            bb, aa = sg.butter(2, [2500 / (SR / 2), 6000 / (SR / 2)], btype='band')
            y = y + sg.lfilter(bb, aa, nz) * np.max(np.abs(y))
        if rng.random() < 0.12:
            env *= 0.15
        out[i:j] = y * env
        i = j
    b, a = sg.butter(3, [300 / (SR / 2), 3400 / (SR / 2)], btype='band')
    out = sg.lfilter(b, a, out)
    return out / np.max(np.abs(out))

def alarm():
    n = int(SR * 0.72); t = np.arange(n) / SR
    f = np.where((t // 0.12) % 2 == 0, 880.0, 660.0)
    s = sum(np.sin(2 * np.pi * f * k * t) / k for k in (1, 3, 5))
    s *= np.minimum(1, t / 0.005) * np.exp(-t / 0.5)
    return s / np.max(np.abs(s))

def thump():
    n = int(SR * 0.25); t = np.arange(n) / SR
    s = np.sin(2 * np.pi * (55 + 30 * np.exp(-t / 0.03)) * t) * np.exp(-t / 0.08)
    return s / np.max(np.abs(s))

def main(dest, dur):
    out = np.zeros(int(SR * (dur + 2)))
    def add(sig, t0, g):
        i = int(t0 * SR); out[i:i + len(sig)] += sig * g
    add(ping(), 0.32, 0.22)
    add(click(7), PLAY0 - 0.04, 0.3)
    add(babble(PLAY1 - PLAY0), PLAY0 + 0.02, 0.34)
    add(ping(), 1.62, 0.2)
    add(whoosh(d=0.16, seed=41), R - 0.14, 0.15)
    add(alarm(), R, 0.26)
    add(boom(), R + 0.2, 0.6)
    add(pop(), R + 0.3, 0.14)
    k = 0
    for tt in np.linspace(TYPE0, TYPE1 - 0.03, 16):
        add(click(200 + k, d=0.02), tt, 0.10); k += 1
    add(whoosh(d=0.14, seed=42, lo=1500, hi=7000), TYPE1, 0.12)
    add(pop(1100, 700), TYPE1 + 0.08, 0.13)
    add(ping(), TY, 0.12)
    add(thump(), TY + 0.25, 0.5); add(thump(), TY + 0.8, 0.5)
    add(boom(), TYEND + 0.1, 0.4)
    add(pop(), TYEND + 0.1, 0.13); add(pop(), TYEND + 0.35, 0.12); add(pop(), TYEND + 0.55, 0.12)
    add(whoosh(d=0.3, seed=43, lo=400, hi=3000), K - 0.08, 0.14)
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
