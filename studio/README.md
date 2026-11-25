# RUTA 100K · générateur de visuels

Un fichier JSON par post dans `posts/`, un PNG par slide dans `out/`. La charte (couleurs, typo, grille) est dans `brand/`, la mise en page dans `templates/`. Aucun texte n'est dans le code : on écrit le JSON, le script rend.

## Installation

```
pip install playwright jinja2 pillow
python -m playwright install chromium
```

Si Chrome est déjà installé, le script l'utilise directement (variable `RUTA_CHROME` pour forcer un chemin).

## Utilisation

```
python render.py posts/2026-11-24_p1_stack.json
python render.py posts/*.json
```

Sorties dans `out/<id du post>/` :

- `ig/NN.png` : Instagram, 1080 x 1350 (4:5)
- `tt/NN.png` : TikTok, 1080 x 1920 (9:16), slide posée hors de la zone légende et boutons
- `planche.png` : planche contact pour relire d'un coup d'œil
- pour un Reel (`"kind": "reel_overlays"`) : `overlays/NN_<id>.png`, textes sur fond transparent à poser sur la vidéo

Le script signale `[A CORRIGER]` dès qu'un texte déborde de sa slide. Rien ne se publie dans cet état.

## Types de slides

| type | champs |
| --- | --- |
| `cover_num` | kicker, number, h1, lead, teaser_label, teaser[] |
| `cover_text` | kicker, display[], display_size, h1, lead, teaser_label, teaser[] |
| `tool` | idx, category, paid{name, price}, free{name, desc}, facts[{k, v}], platforms, good, limit |
| `numbered` | kicker, h2, items[{t, d, src}] |
| `tier` | tier (elite, solid, okay, limit, avoid), label, sub, entries[{t, d, src}] |
| `tiers` | blocks[] de tiers, pour deux niveaux sur une slide |
| `tiergrid` | kicker, h2, rows[{tier, label, chips[]}] |
| `summary` | kicker, h2, rows[{paid, free, amt}], total{label, amt}, note |
| `sources` | kicker, h2, items[{t, u}], cta |
| `cta` | kicker, verb, keyword, lead, list[] |
| `text` | kicker, h1, paragraphs[] |

Options communes : `theme` (`dark` ou clair par défaut), `compact` (slide dense), `foot_left`, `foot_right`. Le mot entre `<b>` passe en corail.

## Règles

- 10 slides au maximum par carrousel : c'est la limite de publication par l'API Instagram.
- Chaque chiffre imprimé a une source datée. Pas de source, pas de chiffre.
- Pas de tiret cadratin dans les textes.

Polices sous licence SIL Open Font License (Archivo, IBM Plex Mono), licences dans `brand/fonts/`.

## Version TikTok native

`"kind": "tiktok"` rend des slides plein écran 1080 x 1920 dans `out/<id>/tt/`, texte gardé dans la zone sûre de TikTok.

| type | champs |
| --- | --- |
| `hook` | kicker, lines[], size, sub |
| `punch` | kicker, h, text |
| `num` | kicker, number, number_size, label, text |
| `list` | kicker, h, items[{n, t, d}] |
| `cta` | kicker, verb, keyword, steps[] |

Thèmes : `dark`, `light`, `coral`.

## Couvertures épurées

| kind | type | champs |
| --- | --- | --- |
| `carousel` | `cover_clean` | kicker, lines[], size, sub |
| `carousel` | `cover_vs` | kicker, paid{name, price}, free{name, price}, sub |
| `tiktok` | `vs` | kicker, paid{name, price}, free{name, price}, sub |

Pour TikTok, une couverture phrase utilise `hook` avec `lines` et au plus une `sub` courte.
