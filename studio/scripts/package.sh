#!/usr/bin/env bash
# Assemble les livrables du jour dans dist/
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf dist && mkdir -p dist/RUTA100K_jour1/{P1_stack,P2_tierlist,P3_reel}
cp -r out/2026-11-24_p1_stack/ig dist/RUTA100K_jour1/P1_stack/instagram
cp -r out/2026-11-24_p1_stack/tt dist/RUTA100K_jour1/P1_stack/tiktok
cp -r out/2026-11-24_p2_tierlist/ig dist/RUTA100K_jour1/P2_tierlist/instagram
cp -r out/2026-11-24_p2_tierlist/tt dist/RUTA100K_jour1/P2_tierlist/tiktok
cp -r out/2026-11-24_p3_reel/overlays dist/RUTA100K_jour1/P3_reel/overlays
cp props/calendario_60_dias.pdf dist/RUTA100K_jour1/P3_reel/
cp legendes_jour1.txt dist/RUTA100K_jour1/
(cd dist && zip -qr RUTA100K_jour1.zip RUTA100K_jour1)
# code du générateur, sans dépendances ni sorties
mkdir -p dist/ruta100k-studio
cp -r brand templates posts props render.py README.md dist/ruta100k-studio/
mkdir -p dist/ruta100k-studio/scripts && cp scripts/package.sh dist/ruta100k-studio/scripts/
rm -f dist/ruta100k-studio/props/*.png
(cd dist && zip -qr ruta100k-studio.zip ruta100k-studio)
cp out/2026-11-24_p1_stack/planche.png dist/P1_planche.png
cp out/2026-11-24_p2_tierlist/planche.png dist/P2_planche.png
ls -la dist | awk '{print $5, $9}'
