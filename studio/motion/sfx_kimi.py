#!/usr/bin/env python3
"""Bruitages du reel KIMI (ChatGPT Pro 500 vs Kimi K3.1 Pro). Synthèse pure.
  python sfx_kimi.py out.wav 13.2
"""
import sys, wave
import numpy as np
from scipy.signal import butter, lfilter
from sfx_gratis import SR, whoosh, ding, boom
from sfx_burger import pop, click
from sfx_clave import ping, thump

PR0, PR1, Y6K, BOT, VS, GR = 0.08, 0.45, 0.48, 0.55, 0.82, 1.15
BE = 1.8
BAR = [BE + 0.3 + i * 0.16 for i in range(5)]
CROWN, G2 = BE + 1.35, BE + 1.45
DM0 = BE + 2.8
D = [DM0 + 0.15, DM0 + 1.3, DM0 + 2.45]
SH = DM0 + 3.65
K = SH + 1.95


def vroom(d=0.8):
    t = np.arange(int(SR * d)) / SR
    f = 70 + 170 * (t / d) ** 1.4
    ph = 2 * np.pi * np.cumsum(f) / SR
    saw = 2 * (ph / (2 * np.pi) % 1) - 1
    b, a = butter(2, 1400 / (SR / 2), 'low')
    s = lfilter(b, a, saw + 0.3 * np.sin(2 * ph))
    env = np.minimum(1, t / 0.05) * np.minimum(1, (d - t) / 0.12)
    return s * env


def main(dest, dur):
    out = np.zeros(int(SR * (dur + 2)))

    def add(sig, t0, g):
        i = int(t0 * SR); out[i:i + len(sig)] += sig * g

    add(whoosh(d=0.28, seed=111, lo=500, hi=4500), 0.0, 0.14)
    add(pop(1200, 700), 0.04, 0.12)
    k = 0
    for tt in np.linspace(PR0, PR1 - 0.02, 11):
        add(click(1500 + k, d=0.015), tt, 0.08); k += 1
    add(ding(2093.0, d=0.5), PR1, 0.16)
    add(thump(), Y6K, 0.3)
    add(whoosh(d=0.26, seed=112, lo=500, hi=4500), BOT - 0.02, 0.14)
    add(boom(), VS, 0.6)
    add(pop(900, 500), VS, 0.12)
    add(pop(1300, 800), GR, 0.13)
    add(ding(2637.02, d=0.6), GR + 0.02, 0.18)
    add(whoosh(d=0.3, seed=113, lo=400, hi=3500), BE - 0.04, 0.15)
    add(pop(), BE + 0.12, 0.11)
    for i, t in enumerate(BAR):
        add(pop(800 + 90 * i, 520 + 60 * i, d=0.07), t, 0.1)
        for tt in np.linspace(t + 0.04, t + 0.5, 6):
            add(click(1600 + k, d=0.012), tt, 0.04); k += 1
    add(ping(), CROWN, 0.16)
    add(boom(), G2, 0.55)
    for f in (1318.51, 1661.22, 1975.53, 2637.02):
        add(ding(f, d=1.3), G2 + 0.02, 0.15)
    add(pop(), G2, 0.12)
    add(whoosh(d=0.34, seed=114, lo=400, hi=3500), DM0 - 0.02, 0.16)
    add(pop(), DM0 + 0.1, 0.11); add(pop(), DM0 + 0.26, 0.11)
    for j, t in enumerate(D):
        add(whoosh(d=0.14, seed=120 + j, lo=1500, hi=7000), t, 0.1)
        add(pop(1100, 700), t + 0.02, 0.11)
        add(ping(), t + 0.3, 0.13)
    add(vroom(), D[0] + 0.38, 0.2)
    add(ding(1567.98, d=0.5), D[0] + 1.12, 0.14)
    add(whoosh(d=1.0, seed=125, lo=250, hi=1800), D[1] + 0.3, 0.09)
    for i, f in enumerate((1046.5, 1318.51, 1567.98, 2093.0)):
        add(ding(f, d=0.35), D[2] + 0.45 + i * 0.1, 0.12)
    add(whoosh(d=0.34, seed=126, lo=400, hi=3500), SH - 0.02, 0.16)
    add(pop(), SH + 0.12, 0.11); add(pop(), SH + 0.3, 0.11)
    for i in range(3):
        add(pop(1100, 700, d=0.08), SH + 0.35 + i * 0.3, 0.12)
    add(whoosh(d=0.3, seed=127, lo=400, hi=3000), K - 0.08, 0.14)
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
