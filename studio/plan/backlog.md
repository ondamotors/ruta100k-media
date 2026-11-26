# Backlog RUTA 100K

Lire `studio/STUDIO.md` d'abord. Pour chaque créneau libre, prendre la première entrée non cochée de son pilier. Une fois programmée : cocher, noter l'heure et l'id Metricool. Tout fait d'une slide est vérifié le jour même sur la source officielle, sinon il saute ; une entrée qu'on ne peut pas vérifier passe à la suivante.

Plus de Día, de RETO ni de post CHIFFRES : aucun chiffre du compte n'est publié (décision de Vincent du 25/11).

## Programmé (Metricool relu le 26/11 à 09:50, heure de Paris)

Un update Metricool change l'id, pas l'uuid : se fier à `getScheduledPosts`.

### Ce qui part : Reels, TikTok + Instagram, publication automatique

Depuis le format vidéo du 25/11 au soir : 3 Reels par jour à 18:30, 00:00 et 03:00 Paris (12:30, 18:00 et 21:00 Bogotá), autoPublish true, donc sans notification.

- Jour 26/11 · 18:30 ESTADO (TT 442300570, IG 442300589) · 00:00 PAGO (TT 442284328, IG 442284348) · 03:00 VIDEO (TT 442420592, IG 442420609)
- Jour 27/11 · 18:30 UGC (TT 442421373, IG 442421395) · 00:00 CLIP (TT 442421411, IG 442421436) · 03:00 AUTO (TT 442421452, IG 442421467)
- Jour 28/11 · 18:30 KIMI (TT 442421484, IG 442421494) · 00:00 WEB (TT 442421518, IG 442421544) · 03:00 ENTRENA (TT 442421571, IG 442421594)
- Jour 29/11 et après : aucun Reel programmé (relu jusqu'au 02/12 06:00).

### Ancienne grille, en brouillon

Ces carrousels et vidéos astuces sont en brouillon : ils ne partent pas, mais ils occupent leur créneau et la routine n'y touche pas.

- Jour 25/11 · 23:30 vidéo NICHO (TT 442171693) · 00:30 CODIGO (TT 442171710, IG 442171730) · 02:30 DINERO (TT 442172210, IG 442172221) : dates passées, jamais publiés
- Jour 26/11 · 18:30 APP (TT 442172238, IG 442172256) · 23:30 vidéo ALGORITMO (TT 442172275) · 00:30 SEO (TT 442184406), INGLES (IG 442184452) · 02:30 COBRAR (IG 442184463)
- Jour 27/11 · 18:30 COMFYUI (TT 442184478, IG 442184496) · 23:30 vidéo PARATI (TT 442185162) · 00:30 PAGO (TT 442185174), TRIAL (IG 442185188) · 02:30 ACESTEP (IG 442185200)
- Jour 28/11 · 18:30 CHATTERBOX (TT 442185229, IG 442185245) · 23:30 vidéo PAGO (TT 442185843) · 00:30 tier list ALGORITMO (TT 442185863), ORIGINAL (IG 442185877) · 02:30 ENVIOS (IG 442185893)
- Jour 29/11 · 18:30 UPSCAYL (TT 442185902, IG 442185913) · 23:30 vidéo SEO (TT 442186338) · 00:30 PARATI (TT 442186365), ALCANCE (IG 442186352) · 02:30 UVR (IG 442186379)

Retirés le 25/11 avant publication (jugés faibles par Vincent) : Subtítulos, Prompt, Ganchos, Ideas, Bio, la vidéo Studio, ESTADO et GOOGLE (ESTADO est revenu en Reel le 26/11). Remplacés par la ligne IA de malade : STUDIO, NICHO, CODIGO, DINERO, APP, INGLES.

Publiés : Día 1 (24/11), Stack (STACK), Algoritmo de TikTok (ALGORITMO), tier list Instagram ; le 25/11, STUDIO en carrousel à 17:54 (TT 442017692, IG 442017709) et en Reel à 20:20 (TT 442198193, IG 442198066) ; le 26/11 à 00:00, Reel GRATIS (TT 442275929, IG 442275941).

Mots-clés déjà pris, jamais réutilisés : STACK, PROMPT, GANCHOS, IDEAS, ALGORITMO, SUBTITULOS, BIO, SEO, STUDIO (avant/après, guía Nano Banana), PAGO, PARATI, COBRAR, TRIAL, ORIGINAL, ENVIOS, ALCANCE, COMFYUI, CHATTERBOX, ACESTEP, UPSCAYL, UVR, ESTADO, GOOGLE, APP, NICHO, CODIGO, DINERO, BANANA, INGLES, DENTRO, MENU, GRATIS, CLAVE, CLIP, UGC, AUTO, WEB, ENTRENA, KIMI, VIDEO.

## À produire à partir du jour 30/11

### IA DE PAGO → IA GRATIS · 18:30, TikTok + Instagram

Modèles : `posts/2026-11-27_p20_comfyui.json` et `_tiktok.json`. Couverture `cover_vs` / `vs`, prix de liste lu sur la page officielle, limite honnête en avant-dernière slide.
- [ ] ChatGPT Plus → LM Studio (modèles ouverts dans ton ordinateur) · mot LMSTUDIO · prix de Plus sur une page OpenAI lisible (sinon entrée suivante), licence et usage commercial sur lmstudio.ai, limite : modèles locaux moins forts, RAM nécessaire. Attention : proche du Reel KIMI (ChatGPT de pago → gratis, 28/11 18:30), prendre l'angle « sin internet, en tu computador ».
- [ ] Runway → Wan 2.2 (vidéo avec IA) · mot WAN · prix Runway sur runwayml.com/pricing, licence Wan sur sa fiche officielle, limite : carte graphique et temps de rendu. Attention : même sujet que le Reel VIDEO (Veo → LTX-2.5, 27/11 03:00), trouver un autre angle ou passer à l'entrée suivante.
- [ ] Topaz Video → Video2X · mot VIDEO2X · prix Topaz Video sur topazlabs.com/pricing, licence et OS sur le GitHub officiel de Video2X, limite : vitesse, carte graphique.

### Vidéo astuce TikTok · 23:30, notification

Faits déjà vérifiés dans les posts de la semaine, aucune nouvelle recherche. Modèles : `posts/2026-11-25_v1_hora_publicar_video.json` et suivants.
- [ ] ComfyUI : glisser une image faite avec ComfyUI redonne tout son workflow · renvoie à COMFYUI
- [ ] Chatterbox : démo officielle dans le navigateur, sans rien installer · renvoie à CHATTERBOX
- [ ] Upscayl : une photo agrandie 4x avec IA, gratis · renvoie à UPSCAYL

### ALGO TIKTOK · 00:30, TikTok seulement

- [ ] Hashtags : ce que TikTok dit vraiment de leur usage (centre d'aide et Creator Academy) · mot HASHTAGS
- [ ] Creative Center : l'outil officiel où TikTok montre les sons, hashtags et créateurs en tendance, pas à pas · mot TENDENCIAS
- [ ] Mode photo : ce que TikTok permet pour les carrousels (nombre de photos, musique, texte) · mot FOTOS

### ALGO INSTAGRAM · 00:30, Instagram seulement

- [x] Recherche Instagram · fait le 25/11 avec Google : « Tu reel en Google », mot GOOGLE, IG 27/11 00:30 (441592768)
- [ ] Hashtags sur Instagram : la règle et la limite actuelles, d'après Instagram · mot ETIQUETAS
- [ ] Durée des Reels : ce qu'Instagram recommande aux non-abonnés selon la durée (n'affirmer que ce qu'Instagram ou Mosseri ont publié) · mot DURACION

### VISTAS ou DINERO · 02:30, Instagram seulement

- [ ] VISTAS · Calendrier de 30 jours de contenu : type de post, idée tirée de `recursos/30-ideas.md`, objectif (guardar, comentar, seguir). Aucun chiffre · mot CALENDARIO
- [ ] VISTAS · Posts collaboratifs : apparaître dans le feed d'un autre compte, comment ça marche d'après Instagram · mot COLLAB
- [ ] DINERO · Marketplace créateurs d'Instagram : où les marques cherchent des créateurs, conditions officielles · mot MARCAS

## Réserve

Quand il reste moins de 6 entrées à produire, en ajouter 6 en respectant les piliers et les créneaux de STUDIO.md, en partant des posts qui ont le mieux marché dans Metricool (jamais Google Drive). Les chiffres servent à choisir, jamais à publier.

## Format à tester plus tard (seulement avec le feu vert de Vincent)

Référence : les Reels de @mavgpt. Visage de Vincent en gros plan sans parler, une bulle blanche de 1 ou 2 lignes en haut, le mot-clé à commenter en très gros au centre, même cadrage à chaque post. Prérequis : une série de plans muets de Vincent. La bulle porte une astuce pour leurs 100K, jamais un chiffre du compte.
