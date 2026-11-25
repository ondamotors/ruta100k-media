#!/usr/bin/env python3
"""Rendu image par image d'une animation HTML (GSAP, timeline en pause pilotée par window.seek).

  python render_motion.py studio.html out.mp4                 vidéo complète 1080x1920, 30 i/s
  python render_motion.py studio.html stills.png 0.4 3.5 6.9  planche d'images fixes à ces instants
"""
import io
import pathlib
import subprocess
import sys

from PIL import Image
from playwright.sync_api import sync_playwright

FPS = 30


def open_page(p, html):
    exe = "/usr/bin/google-chrome" if pathlib.Path("/usr/bin/google-chrome").exists() else None
    browser = p.chromium.launch(executable_path=exe, args=["--no-sandbox", "--disable-gpu-vsync"]) if exe else p.chromium.launch()
    page = browser.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
    page.goto(pathlib.Path(html).resolve().as_uri())
    page.wait_for_function("document.body.dataset.ready === '1'")
    page.wait_for_function("Array.from(document.images).every(i => i.complete && i.naturalWidth > 0)")
    return browser, page


def shot(page, t):
    page.evaluate("(t) => window.seek(t)", t)
    return page.screenshot(type="jpeg", quality=92)


def stills(html, dest, times):
    with sync_playwright() as p:
        browser, page = open_page(p, html)
        ims = [Image.open(io.BytesIO(shot(page, t))).resize((360, 640), Image.LANCZOS) for t in times]
        browser.close()
    sheet = Image.new("RGB", (len(ims) * 370 - 10, 640), (200, 200, 200))
    for k, im in enumerate(ims):
        sheet.paste(im, (k * 370, 0))
    sheet.save(dest)


def video(html, dest):
    dest = pathlib.Path(dest)
    tmp = dest.with_name(dest.stem + ".tmp.mp4")
    with sync_playwright() as p:
        browser, page = open_page(p, html)
        dur = page.evaluate("window.DURATION")
        n = int(round(dur * FPS))
        enc = subprocess.Popen(
            ["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
             "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-shortest",
             "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-crf", "18", "-preset", "veryfast", "-pix_fmt", "yuv420p",
             "-r", str(FPS), "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", str(tmp)],
            stdin=subprocess.PIPE)
        for i in range(n):
            enc.stdin.write(shot(page, i / FPS))
        enc.stdin.close()
        enc.wait()
        browser.close()
    if enc.returncode != 0:
        raise SystemExit("ffmpeg a échoué")
    tmp.rename(dest)
    print(f"OK {dest} ({n} images, {dur:.1f} s)")


if __name__ == "__main__":
    html, dest, *ts = sys.argv[1:]
    if ts:
        stills(html, dest, [float(t) for t in ts])
    else:
        video(html, dest)
