# RUTA 100K · Studio : règles de production

À lire en entier avant de produire quoi que ce soit. Ligne éditoriale revue par Vincent le 25/11/2026.

## Le compte

- RUTA 100K | Crecer con IA. TikTok @ruta100k et Instagram @ruta100k.latam, connectés à Metricool.
- Espagnol latino neutre, tutoiement.
- Le compte donne aux gens les clés pour faire LEURS 100K. On ne parle pas des 100K de Vincent, on ne raconte pas son défi, et on ne publie aucun chiffre du compte (vues, abonnés, likes) jusqu'à nouvel ordre.
- Vincent peut apparaître dans des vidéos mais ne parle jamais face caméra. Pas de vidéo de lui pour l'instant.

## Ce qu'on publie

Des posts qui apprennent quelque chose de fort et donnent envie de demander la suite en commentaire :
1. **ALGO TIKTOK** : ce que TikTok a confirmé sur sa recommandation, la recherche, ce qui sort un post du Pour toi. TikTok seulement.
2. **ALGO INSTAGRAM** : la même chose pour Instagram (Mosseri, Instagram Creators, Meta). Instagram seulement. Jamais un post Instagram sur TikTok, ni l'inverse.
3. **IA DE PAGO → IA GRATIS** : une app d'IA payante, son prix, et l'alternative gratuite, une paire par post. Les deux réseaux.
4. **DINERO** : comment les plateformes paient les créateurs, avec les conditions officielles, et ce que coûtent vraiment les outils. Selon le sujet, un réseau ou les deux.
5. **VISTAS** : ressources pour faire plus de vues (prompts, accroches, idées, bio, sous-titres). Les deux réseaux.

## Lignes rouges

- Aucun chiffre, résultat, témoignage, partenariat ou preuve inventé. Chaque fait sur une slide est vérifié pendant la production sur une source officielle ouverte (WebFetch), sinon il saute. Les prix viennent de la page de prix officielle, avec la date de vérification en pied.
- Jamais de « like si… », « sígueme y te sigo », promesse de follow-back, bots, groupes d'engagement : TikTok rend ces contenus inéligibles au Pour toi et peut sortir tout le compte des recommandations.
- Toute ressource promise existe dans `recursos/` avant que le post soit programmé.
- Jamais de logo de marque dans les visuels : les noms des outils sont composés dans notre typo.
- Jamais de tiret cadratin. Pas d'emoji dans les slides.
- Rien n'est publié hors Metricool. Aucun DM, aucun commentaire au nom de Vincent.
- Ne jamais chercher dans Google Drive, Gmail, Slack ou Notion : ce sont des comptes professionnels sans rapport avec RUTA 100K.

## Créneaux

Metricool : brand 8343331, timezone Europe/Paris, réseaux tiktok et instagram. Heures de Paris pour le jour N (Bogotá = Paris moins 6 h) :

| Réseau | 18:30 (jour N) | 23:30 (jour N) | 00:30 (N+1) | 02:30 (N+1) |
| --- | --- | --- | --- | --- |
| TikTok | IA DE PAGO → GRATIS ou DINERO, carrousel natif | vidéo astuce, en notification | ALGO TIKTOK, carrousel natif | rien |
| Instagram | même sujet que TikTok 18:30, carrousel 4:5 | rien | ALGO INSTAGRAM, carrousel 4:5 | VISTAS ou DINERO, carrousel 4:5 |

Un créneau est pris, réseau par réseau, s'il existe déjà un post programmé à moins de 20 minutes sur ce réseau. Un post réservé à une plateforme est noté « TikTok seulement » ou « Instagram seulement » dans le backlog et n'est jamais dupliqué.

## La première slide

C'est elle qui décide si on s'arrête. Elle doit se comprendre en un coup d'œil :
- 2 à 6 mots en énorme, et au plus une ligne courte en dessous. Rien d'autre : pas de paragraphe, pas de liste, pas de puces, pas de « Día ».
- Types : `cover_clean` (Instagram) ou `hook` (TikTok) pour une phrase ; `cover_vs` (Instagram) ou `vs` (TikTok) pour une paire payant → gratuit (nom barré et prix, flèche, nom gratuit et « US$0 »).
- Les slides suivantes peuvent être plus chargées, juste assez pour qu'on reste quelques secondes, jamais sales.

## Triple accroche, à chaque post

Pour garder les gens le plus longtemps possible :
1. Une première slide qui contredit, choque ou promet, avec un fait vrai.
2. Une slide 2 qui relance (« No lo digo yo, lo dijo TikTok », « no te saltes la 3 »), à varier d'un post à l'autre.
3. Un titre et une première ligne de légende qui ouvrent une boucle vers la fin (« La 5 puede sacar tu cuenta del Para ti »).

Puis une relance dans le kicker de chaque slide (« 3 de 5 · no te la saltes »). Jamais d'affirmation invérifiable sur ce que font les autres (« casi nadie la usa », « la que más funciona ») : la relance pousse à lire, elle n'invente pas de fait. Modèle : `posts/2026-11-25_p9_algoritmo_tiktok.json`.

## Mot-clé en commentaire

Chaque post se termine par un mot-clé à commenter pour obtenir une info en plus, réelle et prête dans `recursos/`. ManyChat ne peut pas se brancher sur un compte TikTok basé dans l'UE et rien n'est automatisé sur Instagram : Vincent livre à la main en DM.
- Dernière slide : type `cta`, verb « Comenta », keyword en majuscules, puis « Escríbeme MOT por mensaje » et « Solo para seguidores ».
- Légende : d'abord les mots que les gens tapent dans la recherche, la boucle vers la fin, puis « ¿Lo quieres? Comenta MOT, sígueme y escríbeme MOT por mensaje. » (« por DM » sur Instagram), puis 3 hashtags.
- Ressource `recursos/<slug>.md` (même style que les existantes) et sa ligne dans `recursos/README.md` (mot-clé, lien GitHub, réponse DM prête à coller). Un mot-clé = une seule ressource, jamais réutilisé.

## Deux versions par post

- Instagram : carrousel 4:5 (kind `carousel`, `<date>_p<N>_<slug>.json`), export `instagram/NN.jpg` depuis `out/<id>/ig/`, 10 images au maximum.
- TikTok : carrousel natif plein écran (kind `tiktok`, `<date>_p<N>_<slug>_tiktok.json`), export `tiktok/NN.jpg` depuis `out/<id>/tt/`. Une idée par slide, 12 mots maximum hors listes, 5 à 9 slides, ton oral et direct.

## Vidéo astuce TikTok (23:30)

- 4 à 6 scènes de 1,4 à 2 s, 7 à 10 s au total, kind `tiktok_video` (mêmes types de scène que la version TikTok native, plus `dur`). Une seule astuce vérifiée, la triple accroche dès la scène 1, et la dernière scène renvoie vers un mot-clé ou vers le compte.
- Rendu : `cd studio && python3 video.py posts/<fichier>.json`, zéro « [A CORRIGER] », puis ouvrir `out/<id>/planche.png` avec Read. Export `video.mp4` et `cover.jpg` vers `<date>/p<N>_<slug>/tiktok/`.
- Metricool : providers tiktok, media = URL raw du `video.mp4` au SHA du commit, **autoPublish false** (Vincent reçoit une notif, ajoute un son dans TikTok et publie), tiktokData { privacyOption PUBLIC_TO_EVERYONE, title, isAigc false }.

## Produire un post

1. JSON dans `studio/posts/`. Schémas : `studio/README.md`. Modèles : les posts existants.
2. Rendu : `cd studio && python3 render.py posts/<fichier>.json`. Zéro ligne « [A CORRIGER] » : raccourcir ou ajouter `"compact": true`. Puis ouvrir `out/<id>/planche.png` avec Read et vérifier chaque slide à l'œil, la première surtout.
3. Export JPEG qualité 92 à la racine du dépôt : `<AAAA-MM-JJ>/p<N>_<slug>/tiktok/NN.jpg` et `.../instagram/NN.jpg`.
4. Commit avec `git -c user.name="RUTA 100K" -c user.email="studio@ruta100k.invalid"`, jamais d'adresse personnelle. Push sur main.
5. Metricool `createScheduledPost`, une fois par réseau au créneau prévu, media = `https://raw.githubusercontent.com/ondamotors/ruta100k-media/<SHA du commit>/<chemin>` (le SHA, jamais main), autoPublish true sauf la vidéo :
   - TikTok : providers tiktok, tiktokData { privacyOption PUBLIC_TO_EVERYONE, title de 90 caractères maximum, autoAddMusic true, photoCoverIndex 0 }.
   - Instagram : providers instagram, instagramData { type POST, isAiGenerated false }.
6. Dans `studio/plan/backlog.md`, cocher l'entrée et noter l'id Metricool et l'heure.
