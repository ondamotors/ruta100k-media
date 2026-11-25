#!/usr/bin/env python3
"""Bruitages du reel burger (MENU), calés sur la timeline de burger.html. Synthèse pure, réutilise sfx_gratis.
  python sfx_burger.py out.wav 14.0
"""
import sys, wave
import numpy as np
import scipy.signal as sg
from sfx_gratis import SR, whoosh, ding, boom

def pop(f0=900, f1=480, d=0.09):
    n = int(SR * d); t = np.arange(n) / SR
    f = f1 + (f0 - f1) * np.exp(-t / 0.025)
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.03)
    return s / np.max(np.abs(s))

def click(seed=5, d=0.03):
    n = int(SR * d); t = np.arange(n) / SR
    x = np.random.default_rng(seed).standard_normal(n)
    b, a = sg.butter(2, [1800 / (SR / 2), 7000 / (SR / 2)], btype='band')
    x = sg.lfilter(b, a, x) * np.exp(-t / 0.006)
    return x / np.max(np.abs(x))

def main(dest, dur):
    out = np.zeros(int(SR * (dur + 2)))
    def add(sig, t0, g):
        i = int(t0 * SR); out[i:i + len(sig)] += sig * g
    add(click(1), 0.42, 0.35)                                   # tap sur la photo
    add(whoosh(d=0.2, seed=21), 0.68, 0.16)                     # montée vers le flash
    add(boom(), 0.87, 0.7)                                      # révélation
    for f in (1318.51, 1661.22, 1975.53):
        add(ding(f, d=1.2), 0.88, 0.12)
    add(pop(), 0.95, 0.16); add(pop(1000, 560), 1.30, 0.14)     # « IA GRATIS », « nivel comercial »
    add(whoosh(d=0.24, seed=22), 1.92, 0.15)                    # vers l'écran
    add(pop(), 2.20, 0.14); add(pop(), 2.68, 0.14)              # étapes 1 et 2
    add(click(2), 3.62, 0.3)                                    # envoi
    add(pop(1000, 560), 4.08, 0.14)                             # « 34 segundos después »
    t, gap = 4.12, 0.11                                         # tic-tac qui accélère pendant l'attente
    while t < 5.02:
        add(click(int(t * 100)), t, 0.22); t += gap; gap = max(0.045, gap * 0.86)
    add(ding(2637.02, d=0.9), 5.10, 0.26)                       # « 3. Listo ✨ »
    for f in (1975.53, 3135.96):
        add(ding(f, d=0.9), 5.13, 0.1)
    add(whoosh(d=0.2, seed=23), 6.88, 0.16)
    add(boom(), 7.05, 0.45)                                     # résultat plein écran
    add(ding(1975.53, d=0.5), 7.2, 0.2); add(ding(2637.02, d=0.8), 7.32, 0.24)   # « a restaurantes 💸 »
    add(pop(), 8.95, 0.14)
    add(whoosh(d=1.0, seed=24, lo=300, hi=2500), 9.25, 0.13)   # curseur avant/après
    add(whoosh(d=0.2, seed=25), 10.7, 0.15)
    add(boom(), 10.86, 0.35)                                    # CTA
    add(pop(), 10.92, 0.14); add(pop(), 11.15, 0.14)
    add(ding(1975.53, d=0.7), 11.35, 0.22)                      # « MENU »
    add(pop(1000, 560), 11.70, 0.12)
    out = out[:int(SR * dur)]
    fade = int(SR * 0.08); out[-fade:] *= np.linspace(1, 0, fade)
    out = out / np.max(np.abs(out)) * 0.70
    pcm = (out * 32767).astype(np.int16)
    with wave.open(dest, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(np.repeat(pcm[:, None], 2, axis=1).tobytes())
    print('OK', dest, f'{dur:.2f} s')

if __name__ == '__main__':
    main(sys.argv[1], float(sys.argv[2]))
