#!/usr/bin/env python3
"""Son du reel CLAVE v2 : la vraie note vocale (fichier fourni par Vincent) + bruitages synthétisés.
  python sfx_clave2.py voz.wav out.wav 16.2
"""
import sys, wave
import numpy as np
import scipy.signal as sg
from sfx_gratis import SR, whoosh, ding, boom
from sfx_burger import pop, click
from sfx_clave import ping, alarm, thump

PLAY0 = 0.62
M2 = 3.37
R = 7.7
TYPE0, TYPE1 = 9.35, 9.85
TY, TYEND = 10.15, 11.15
K = 13.0

def load_voice(path):
    w = wave.open(path)
    sr, ch = w.getframerate(), w.getnchannels()
    x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(float) / 32768
    if ch > 1:
        x = x.reshape(-1, ch).mean(axis=1)
    if sr != SR:
        g = np.gcd(SR, sr)
        x = sg.resample_poly(x, SR // g, sr // g)
    b, a = sg.butter(2, [110 / (SR / 2), 9000 / (SR / 2)], btype='band')
    x = sg.lfilter(b, a, x)
    return x / np.max(np.abs(x))

def main(voice, dest, dur):
    out = np.zeros(int(SR * (dur + 2)))
    def add(sig, t0, g):
        i = int(t0 * SR); out[i:i + len(sig)] += sig * g
    add(ping(), 0.32, 0.2)
    add(click(7), PLAY0 - 0.04, 0.25)
    add(load_voice(voice), PLAY0, 0.92)                      # la vraie note vocale
    add(pop(), 1.95, 0.08)                                    # « súbele el volumen »
    add(ping(), M2, 0.1)
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
    add(thump(), TY + 0.2, 0.5); add(thump(), TY + 0.7, 0.5)
    add(boom(), TYEND + 0.1, 0.4)
    add(pop(), TYEND + 0.1, 0.13); add(pop(), TYEND + 0.35, 0.12)
    add(whoosh(d=0.3, seed=43, lo=400, hi=3000), K - 0.08, 0.14)
    add(boom(), K, 0.35)
    add(pop(), K + 0.06, 0.13); add(pop(), K + 0.3, 0.13)
    add(ding(1975.53, d=0.7), K + 0.5, 0.22)
    add(pop(1000, 560), K + 0.85, 0.11); add(pop(1000, 560), K + 1.05, 0.1)
    out = out[:int(SR * dur)]
    fade = int(SR * 0.06); out[-fade:] *= np.linspace(1, 0, fade)
    out = out / np.max(np.abs(out)) * 0.89
    pcm = (out * 32767).astype(np.int16)
    with wave.open(dest, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(np.repeat(pcm[:, None], 2, axis=1).tobytes())
    print('OK', dest, f'{dur:.2f} s')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], float(sys.argv[3]))
