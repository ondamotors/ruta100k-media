#!/usr/bin/env python3
"""RUTA 100K · générateur de visuels.

Un fichier JSON par post (dossier posts/) -> PNG prêts à publier.
  python render.py posts/2026-11-24_p1_stack.json          carrousel : Instagram 4:5 + TikTok 9:16 + planche contact
  python render.py posts/2026-11-24_p3_reel.json           overlays de Reel : PNG transparents 1080x1920
  python render.py posts/*.json                            tout le dossier

Sorties dans out/<id>/ : ig/NN.png (1080x1350), tt/NN.png (1080x1920), planche.png, et pour un Reel overlays/NN.png.
Le script signale toute slide dont le contenu déborde : on ne publie rien qui dépasse.
"""
import json
import os
import pathlib
import shutil
import sys

from jinja2 import Environment, FileSystemLoader, select_autoescape
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "out"
INK, PAPER = (13, 13, 13), (241, 241, 239)
TT_OFFSET_Y = 170  # carrousel TikTok : la slide 4:5 est posée haut, hors de la zone légende/boutons


def chrome_path():
    """Chrome système si présent (Windows, macOS, Linux), sinon le Chromium de Playwright."""
    candidates = [
        os.environ.get("RUTA_CHROME", ""),
        "/usr/bin/google-chrome",
        "/usr/bin/chromium",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]
    return next((c for c in candidates if c and pathlib.Path(c).exists()), None)


def overflow_report(page, height):
    return page.evaluate(
        """(h) => {
          const issues = [];
          const slide = document.querySelector('.slide, .ovl');
          if (slide && slide.scrollHeight > h + 1) issues.push('hauteur ' + slide.scrollHeight + 'px > ' + h);
          document.querySelectorAll('.body').forEach(b => {
            if (b.scrollHeight > b.clientHeight + 2) issues.push('bloc texte trop haut (' + b.scrollHeight + ' > ' + b.clientHeight + ')');
          });
          document.querySelectorAll('[data-fit]').forEach(el => {
            const rg = document.createRange(); rg.selectNodeContents(el);
            if (rg.getBoundingClientRect().width > el.parentElement.getBoundingClientRect().width + 2) issues.push('titre trop large : ' + el.textContent.trim().slice(0, 30));
          });
          return issues;
        }""",
        height,
    )


def render_post(post_path, browser, env):
    post = json.loads(pathlib.Path(post_path).read_text(encoding="utf-8"))
    out = OUT / post["id"]
    if out.exists():
        shutil.rmtree(out)
    (out / "_html").mkdir(parents=True)
    problems = []

    if post.get("kind") == "reel_overlays":
        tpl = env.get_template("overlay.html.j2")
        (out / "overlays").mkdir()
        page = browser.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
        for i, o in enumerate(post["overlays"], 1):
            f = out / "_html" / f"{i:02d}.html"
            f.write_text(tpl.render(o=o, root=ROOT.as_uri()), encoding="utf-8")
            page.goto(f.as_uri())
            page.wait_for_function("document.body.dataset.ready === '1'")
            problems += [f"overlay {i:02d}: {p}" for p in overflow_report(page, 1920)]
            page.screenshot(path=str(out / "overlays" / f"{i:02d}_{o['id']}.png"), omit_background=True)
        page.close()
        contact_sheet(sorted((out / "overlays").glob("*.png")), out / "planche.png", cols=4, bg=(60, 60, 60))
        shutil.rmtree(out / "_html")
        return out, problems

    tpl = env.get_template("slide.html.j2")
    slides = post["slides"]
    (out / "ig").mkdir()
    (out / "tt").mkdir()
    page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
    for i, s in enumerate(slides, 1):
        f = out / "_html" / f"{i:02d}.html"
        f.write_text(tpl.render(post=post, s=s, i=i, n=len(slides), root=ROOT.as_uri(), W=1080, H=1350), encoding="utf-8")
        page.goto(f.as_uri())
        page.wait_for_function("document.body.dataset.ready === '1'")
        problems += [f"slide {i:02d}: {p}" for p in overflow_report(page, 1350)]
        ig = out / "ig" / f"{i:02d}.png"
        page.screenshot(path=str(ig), clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
        # Version TikTok 9:16 : même slide, posée dans la zone sûre.
        bg = INK if (s.get("theme") == "dark") else PAPER
        canvas = Image.new("RGB", (1080, 1920), bg)
        canvas.paste(Image.open(ig).convert("RGB"), (0, TT_OFFSET_Y))
        canvas.save(out / "tt" / f"{i:02d}.png", optimize=True)
    page.close()
    contact_sheet(sorted((out / "ig").glob("*.png")), out / "planche.png", cols=4)
    shutil.rmtree(out / "_html")
    return out, problems


def contact_sheet(files, dest, cols=4, thumb_w=360, gap=18, bg=(220, 220, 218)):
    if not files:
        return
    ims = [Image.open(f).convert("RGBA") for f in files]
    w0, h0 = ims[0].size
    th = int(thumb_w * h0 / w0)
    rows = (len(ims) + cols - 1) // cols
    sheet = Image.new("RGBA", (cols * thumb_w + (cols + 1) * gap, rows * th + (rows + 1) * gap), bg + (255,))
    for k, im in enumerate(ims):
        r, c = divmod(k, cols)
        t = im.resize((thumb_w, th), Image.LANCZOS)
        sheet.alpha_composite(t, (gap + c * (thumb_w + gap), gap + r * (th + gap)))
    sheet.convert("RGB").save(dest, optimize=True)


def main(paths):
    env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=select_autoescape(["html", "j2"]))
    with sync_playwright() as p:
        exe = chrome_path()
        browser = p.chromium.launch(executable_path=exe, args=["--no-sandbox"]) if exe else p.chromium.launch()
        all_ok = True
        for path in paths:
            out, problems = render_post(path, browser, env)
            status = "OK" if not problems else "A CORRIGER"
            all_ok &= not problems
            print(f"[{status}] {path} -> {out.relative_to(ROOT)}")
            for pb in problems:
                print("   -", pb)
        browser.close()
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    main(sys.argv[1:])
