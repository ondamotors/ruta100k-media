# RUTA 100K · Studio : règles de production

À lire en entier avant de produire quoi que ce soit.

## Le compte

- RUTA 100K, TikTok « RUTA 100K | Crecer con IA » connecté à Metricool. Instagram pas encore connecté.
- Espagnol latino neutre, tutoiement. Défi public : 0 à 100K abonnés du 24/11/2026 au 22/01/2027.
- Día N = date en Amérique latine. Día 1 = 24/11/2026, Día 2 = 25/11/2026, etc.
- Vincent peut apparaître dans des vidéos mais ne parle jamais face caméra. Il a déjà fait grandir d'autres comptes : on le dit, mais aucun chiffre sur ces comptes tant qu'il n'a pas fourni ses captures.
- Promesses publiques déjà faites, à tenir : les chiffres réels chaque dimanche ; chaque semaine, audit public de 3 comptes choisis parmi ceux qui ont commenté DENTRO et qui suivent le compte.

## Lignes rouges

- Aucun chiffre, résultat, témoignage, partenariat ou preuve inventé. Chaque fait sur une slide est vérifié pendant le run sur une source officielle ouverte (WebFetch), sinon il saute.
- Jamais de « like si… », « sígueme y te sigo », promesse de follow-back, bots, groupes d'engagement : TikTok rend ces contenus inéligibles au Pour toi et peut sortir tout le compte des recommandations.
- Toute ressource promise existe dans `recursos/` avant que le post soit programmé.
- Jamais de tiret cadratin. Pas d'emoji dans les slides.
- Rien n'est publié hors Metricool. Aucun DM, aucun commentaire au nom de Vincent.

## Créneaux

Metricool : brand 8343331, timezone Europe/Paris, réseau tiktok.

Día N : 18:30 le jour N, puis 00:30 et 02:30 le jour N+1 (heure de Paris), soit 12:30, 18:30 et 20:30 à Bogotá.

Un créneau est pris s'il existe déjà un post programmé à moins de 20 minutes. Une entrée du backlog à date imposée réserve son créneau : ne rien y mettre d'autre, et ne la produire que le jour indiqué.

## Mix quotidien

1. RESSOURCE : un mot-clé à commenter, follow obligatoire, la ressource part en DM.
2. SOURCE OFFICIELLE ou OUTILS vérifiés : tier list, comparatif, « ce que TikTok a dit ». Fait pour le débat et le partage.
3. RETO : récit du défi, coulisses, chiffres réels tirés de Metricool. Fait pour le follow.

## Mécanique commentaire + follow sur TikTok

ManyChat ne peut pas se brancher sur un compte TikTok basé dans l'UE : Vincent livre les ressources à la main en DM.

- Dernière slide d'un post ressource : type `cta`, verb « Comenta », keyword = le mot-clé en majuscules, lead « Y escríbeme MOT por mensaje: te mando … », list [« Solo para seguidores: sígueme antes de escribir. », « Guárdalo para … »].
- Légende : une phrase de valeur, puis « ¿Lo quieres? Comenta MOT, sígueme y escríbeme MOT por mensaje. », puis 3 ou 4 hashtags de niche.
- Créer la ressource `recursos/<slug>.md` (même style que les existantes, pied RUTA 100K) et ajouter sa ligne dans `recursos/README.md` (mot-clé, lien GitHub, réponse DM prête à coller).
- Un mot-clé = une seule ressource. Ne jamais réutiliser un mot-clé existant.

## Produire un post

1. JSON dans `studio/posts/<AAAA-MM-JJ>_p<N>_<slug>.json`. Schéma : `studio/README.md`. Modèles : les posts existants, dont les longueurs de texte sont calibrées. 6 à 10 slides. Couverture : un chiffre ou une promesse concrète. « Día N » dans le kicker de couverture ou le pied (`foot_left`).
2. Rendu : `cd studio && python3 render.py posts/<fichier>.json`. Zéro ligne « [A CORRIGER] » : raccourcir le texte ou ajouter `"compact": true`. Puis ouvrir `out/<id>/planche.png` avec Read et vérifier chaque slide à l'œil.
3. Export JPEG qualité 92 : `<AAAA-MM-JJ>/p<N>_<slug>/tiktok/NN.jpg` (depuis `out/<id>/tt/`) et `.../instagram/NN.jpg` (depuis `out/<id>/ig/`), à la racine du dépôt.
4. Commit avec `git -c user.name="RUTA 100K" -c user.email="studio@ruta100k.invalid"`, jamais d'adresse personnelle. Push sur main.
5. Metricool `createScheduledPost` : media = `https://raw.githubusercontent.com/ondamotors/ruta100k-media/<SHA du commit>/<chemin>` (le SHA, jamais main), providers tiktok, autoPublish true, tiktokData { privacyOption PUBLIC_TO_EVERYONE, title de 90 caractères maximum, autoAddMusic true, photoCoverIndex 0 }.
6. Dans `studio/plan/backlog.md`, cocher l'entrée et noter l'id Metricool et l'heure.

## Chiffres du défi

Source unique : les analytics Metricool du compte TikTok. On publie les chiffres tels quels, même petits. Jamais d'arrondi à la hausse, jamais d'estimation présentée comme un chiffre.
