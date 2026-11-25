#!/usr/bin/env python3
"""Bruitages du reel VIDEO (Google AI Ultra vs LTX-2.5). Synthèse pure.
  python sfx_ltx.py out.wav 13.4
"""
import sys, wave
import numpy as np
from sfx_gratis import SR, whoosh, ding, boom
from sfx_burger import pop, click
from sfx_clave import ping, thump

PR0, PR1, Y6K, BOT, VS, GR = 0.08, 0.45, 0.48, 0.55, 0.82, 1.15
BE = 1.8
TIL = [BE + 0.25, BE + 0.55, BE + 0.85, BE + 1.15]
DM0 = BE + 2.95
TY0, TY1, GO, P0, P1, DONE = DM0 + 0.25, DM0 + 0.95, DM0 + 1.0, DM0 + 1.05, DM0 + 2.05, DM0 + 2.1
SH = DM0 + 3.65
K = SH + 2.0


def riser(d=1.0):
    t = np.arange(int(SR * d)) / SR
    f = 260 + 700 * (t / d) ** 2
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * (0.6 + 0.4 * np.sin(2 * np.pi * 9 * t))
    return s * np.minimum(1, t / 0.1) * np.minimum(1, (d - t) / 0.05)


def main(dest, dur):
    out = np.zeros(int(SR * (dur + 2)))

    def add(sig, t0, g):
        i = int(t0 * SR); out[i:i + len(sig)] += sig * g

    add(whoosh(d=0.28, seed=131, lo=500, hi=4500), 0.0, 0.14)
    add(pop(1200, 700), 0.04, 0.12)
    k = 0
    for tt in np.linspace(PR0, PR1 - 0.02, 11):
        add(click(1700 + k, d=0.015), tt, 0.08); k += 1
    add(ding(2093.0, d=0.5), PR1, 0.16)
    add(thump(), Y6K, 0.3)
    add(whoosh(d=0.26, seed=132, lo=500, hi=4500), BOT - 0.02, 0.14)
    add(boom(), VS, 0.6)
    add(pop(900, 500), VS, 0.12)
    add(pop(1300, 800), GR, 0.13)
    add(ding(2637.02, d=0.6), GR + 0.02, 0.18)
    add(whoosh(d=0.3, seed=133, lo=400, hi=3500), BE - 0.04, 0.15)
    add(pop(), BE + 0.12, 0.11)
    for i, t in enumerate(TIL):
        add(pop(900 + 120 * i, 600 + 80 * i, d=0.08), t, 0.13)
        add(ding([1318.51, 1567.98, 1975.53, 2637.02][i], d=0.4), t + 0.02, 0.12)
    add(boom(), TIL[3] + 0.05, 0.45)
    add(pop(), BE + 0.95, 0.12)
    add(whoosh(d=0.34, seed=134, lo=400, hi=3500), DM0 - 0.02, 0.16)
    add(pop(), DM0 + 0.1, 0.11); add(pop(), DM0 + 0.26, 0.11)
    for tt in np.linspace(TY0, TY1 - 0.03, 16):
        add(click(1800 + k, d=0.02), tt, 0.08); k += 1
    add(click(1900, d=0.03), GO - 0.04, 0.16)
    add(riser(P1 - P0), P0, 0.07)
    add(boom(1.4), DONE, 0.7)
    add(whoosh(d=0.5, seed=135, lo=200, hi=2500), DONE - 0.05, 0.14)
    for f in (1318.51, 1661.22, 1975.53):
        add(ding(f, d=1.0), DONE + 0.05, 0.12)
    for i in range(4):
        add(pop(1100 + 80 * i, 700, d=0.06), DONE + 0.15 + i * 0.12, 0.1)
    for i in range(3):
        add(pop(800, 500, d=0.06), DONE + 0.2 + i * 0.22, 0.09)
    add(whoosh(d=0.34, seed=136, lo=400, hi=3500), SH - 0.02, 0.16)
    add(pop(), SH + 0.12, 0.11); add(pop(), SH + 0.3, 0.11)
    for i in range(3):
        add(pop(1100, 700, d=0.08), SH + 0.35 + i * 0.3, 0.12)
    add(whoosh(d=0.3, seed=137, lo=400, hi=3000), K - 0.08, 0.14)
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
