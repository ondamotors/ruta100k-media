#!/usr/bin/env python3
"""RUTA 100K · vidéo TikTok native.

Des scènes plein écran (gabarit templates/tiktok.html.j2) -> une vidéo 1080 x 1920, 30 i/s, sans musique :
Vincent ajoute le son dans TikTok au moment de publier.

  python video.py posts/2026-11-26_p10_dia3_video.json

JSON : {"id", "kind": "tiktok_video", "series", "foot_left", "foot_last",
        "scenes": [ {mêmes champs qu'une slide tiktok, "dur": 1.6}, ... ]}

Sorties dans out/<id>/ : frames/NN.png, video.mp4, cover.jpg (première scène), planche.png.
Le script signale "[A CORRIGER]" si un texte déborde de la zone sûre.
"""
import json
import pathlib
import shutil
import subprocess
import sys

from jinja2 import Environment, FileSystemLoader, select_autoescape
from PIL import Image
from playwright.sync_api import sync_playwright

from render import OUT, ROOT, chrome_path, contact_sheet, overflow_report

FPS = 30
ENC = ["-c:v", "libx264", "-crf", "18", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-r", str(FPS)]


def ff(*args):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *args], check=True)


def scene_clip(png, dur, dst, zoom=0.03):
    """Plan fixe avec une poussée lente de 3 % : le texte reste dans la zone sûre."""
    frames = max(1, round(dur * FPS))
    tmp = dst.with_name(dst.stem + ".tmp.mp4")
    vf = (
        "scale=2160:3840,"
        f"zoompan=z='1+{zoom}*on/{frames}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s=1080x1920:fps={FPS},"
        "format=yuv420p"
    )
    ff("-i", str(png), "-vf", vf, "-frames:v", str(frames), *ENC, str(tmp))
    tmp.rename(dst)


def make_video(post_path):
    post = json.loads(pathlib.Path(post_path).read_text(encoding="utf-8"))
    out = OUT / post["id"]
    if out.exists():
        shutil.rmtree(out)
    for d in ("_html", "frames", "_clips"):
        (out / d).mkdir(parents=True)
    env = Environment(loader=FileSystemLoader(str(ROOT / "templates")), autoescape=select_autoescape([]))
    tpl = env.get_template("tiktok.html.j2")
    scenes = post["scenes"]
    problems = []

    with sync_playwright() as p:
        kw = {"executable_path": chrome_path()} if chrome_path() else {}
        browser = p.chromium.launch(**kw)
        page = browser.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
        for i, s in enumerate(scenes, 1):
            f = out / "_html" / f"{i:02d}.html"
            # Pas de « Desliza » dans une vidéo : le pied affiche la série.
            post_v = dict(post, foot_last=post.get("foot_last", ""))
            f.write_text(tpl.render(post=post_v, s=dict(s, foot_left=s.get("foot_left") or post.get("foot_left", "")), i=i, n=len(scenes), root=ROOT.as_uri()), encoding="utf-8")
            page.goto(f.as_uri())
            page.wait_for_function("document.body.dataset.ready === '1'")
            page.evaluate("document.querySelectorAll('.foot span:last-child').forEach(e => e.textContent = '')")
            problems += [f"scène {i:02d}: {x}" for x in overflow_report(page, 1920)]
            page.screenshot(path=str(out / "frames" / f"{i:02d}.png"), clip={"x": 0, "y": 0, "width": 1080, "height": 1920})
        browser.close()

    clips = []
    for i, s in enumerate(scenes, 1):
        dst = out / "_clips" / f"{i:02d}.mp4"
        scene_clip(out / "frames" / f"{i:02d}.png", float(s.get("dur", 1.6)), dst)
        clips.append(dst)
    lst = out / "_clips" / "list.txt"
    lst.write_text("".join(f"file '{c.name}'\n" for c in clips), encoding="utf-8")
    silent = out / "_clips" / "joined.mp4"
    ff("-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(silent))
    # Piste audio muette : Vincent choisit le son dans TikTok.
    tmp = out / "video.tmp.mp4"
    ff("-i", str(silent), "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-shortest",
       "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", str(tmp))
    tmp.rename(out / "video.mp4")

    Image.open(out / "frames" / "01.png").convert("RGB").save(out / "cover.jpg", "JPEG", quality=92)
    contact_sheet(sorted((out / "frames").glob("*.png")), out / "planche.png", cols=6, thumb_w=260)
    shutil.rmtree(out / "_html")
    shutil.rmtree(out / "_clips")
    return out, problems


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    bad = False
    for path in sys.argv[1:]:
        out, problems = make_video(path)
        if problems:
            bad = True
            print(f"[A CORRIGER] {path}")
            for x in problems:
                print("   ", x)
        else:
            dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(out / "video.mp4")],
                                 capture_output=True, text=True).stdout.strip()
            print(f"[OK] {path} -> {out}/video.mp4 ({float(dur):.1f} s)")
    sys.exit(1 if bad else 0)
