# RUTA 100K · Studio : règles de production

À lire en entier avant de produire quoi que ce soit.

## Le compte

- RUTA 100K | Crecer con IA. TikTok @ruta100k et Instagram @ruta100k.latam, tous deux connectés à Metricool. Chaque post sort sur les deux réseaux.
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

Metricool : brand 8343331, timezone Europe/Paris, réseaux tiktok et instagram.

Día N : 18:30 le jour N, puis 00:30 et 02:30 le jour N+1 (heure de Paris), soit 12:30, 18:30 et 20:30 à Bogotá.

Un créneau est pris, réseau par réseau, s'il existe déjà un post programmé à moins de 20 minutes sur ce réseau. Une entrée du backlog à date imposée réserve son créneau : ne rien y mettre d'autre, et ne la produire que le jour indiqué.

## Mix quotidien

1. RESSOURCE : un mot-clé à commenter, follow obligatoire, la ressource part en DM.
2. SOURCE OFFICIELLE ou OUTILS vérifiés : tier list, comparatif, « ce que TikTok a dit ». Fait pour le débat et le partage.
3. RETO : récit du défi, coulisses, chiffres réels tirés de Metricool. Fait pour le follow.

## Mécanique commentaire + follow

ManyChat ne peut pas se brancher sur un compte TikTok basé dans l'UE, et rien n'est encore automatisé sur Instagram : Vincent livre les ressources à la main en DM sur les deux réseaux.

- Dernière slide d'un post ressource : type `cta`, verb « Comenta », keyword = le mot-clé en majuscules, lead « Y escríbeme MOT por mensaje: te mando … », list [« Solo para seguidores: sígueme antes de escribir. », « Guárdalo para … »].
- Légende : une phrase de valeur, puis « ¿Lo quieres? Comenta MOT, sígueme y escríbeme MOT por mensaje. », puis 3 ou 4 hashtags de niche.
- Créer la ressource `recursos/<slug>.md` (même style que les existantes, pied RUTA 100K) et ajouter sa ligne dans `recursos/README.md` (mot-clé, lien GitHub, réponse DM prête à coller).
- Un mot-clé = une seule ressource. Ne jamais réutiliser un mot-clé existant.

## TikTok natif

Un carrousel pensé pour Instagram ne suffit pas sur TikTok. Chaque post a donc deux versions :
- Instagram : la version éditoriale 4:5 (kind `carousel`, `<date>_p<N>_<slug>.json`), export `instagram/NN.jpg` depuis `out/<id>/ig/`.
- TikTok : une version native plein écran (kind `tiktok`, `<date>_p<N>_<slug>_tiktok.json`, gabarit `templates/tiktok.html.j2`), export `tiktok/NN.jpg` depuis `out/<id>/tt/`. Modèle : `posts/_exemple_tiktok_stack.json`.

Règles de la version TikTok :
- Une idée par slide, 12 mots maximum hors listes, 5 à 8 slides. Types : hook, punch, num, list, cta. Thèmes dark, light, coral.
- La couverture arrête le pouce : un chiffre énorme, une contradiction ou une promesse concrète, jamais une phrase de contexte.
- Ton oral et direct, phrases courtes (« Ojo », « Nadie te lo dice »). « POV » seulement si c'est vrai.
- Le gabarit garde le texte dans la zone sûre (boutons à droite, légende en bas) : ne jamais le contourner avec du style en ligne.
- Légende TikTok : d'abord les mots que les gens tapent dans la recherche, puis l'appel à l'action, puis 3 hashtags.
- Le post RETO du jour sur TikTok devient la série « Día N/60 », toujours au même gabarit : couverture `num` avec le vrai nombre d'abonnés lu dans Metricool, puis la leçon du jour. La série doit se reconnaître d'un coup d'œil et donner envie de voir la suite.

## Produire un post

1. JSON dans `studio/posts/<AAAA-MM-JJ>_p<N>_<slug>.json`. Schéma : `studio/README.md`. Modèles : les posts existants, dont les longueurs de texte sont calibrées. 6 à 10 slides. Couverture : un chiffre ou une promesse concrète. « Día N » dans le kicker de couverture ou le pied (`foot_left`).
2. Rendu : `cd studio && python3 render.py posts/<fichier>.json`. Zéro ligne « [A CORRIGER] » : raccourcir le texte ou ajouter `"compact": true`. Puis ouvrir `out/<id>/planche.png` avec Read et vérifier chaque slide à l'œil.
3. Export JPEG qualité 92 à la racine du dépôt : `<AAAA-MM-JJ>/p<N>_<slug>/tiktok/NN.jpg` depuis la version TikTok native (`out/<id>_tiktok/tt/`) et `.../instagram/NN.jpg` depuis la version Instagram (`out/<id>/ig/`).
4. Commit avec `git -c user.name="RUTA 100K" -c user.email="studio@ruta100k.invalid"`, jamais d'adresse personnelle. Push sur main.
5. Metricool `createScheduledPost`, deux fois au même créneau, avec media = `https://raw.githubusercontent.com/ondamotors/ruta100k-media/<SHA du commit>/<chemin>` (le SHA, jamais main) et autoPublish true :
   - TikTok : images `tiktok/NN.jpg`, providers tiktok, tiktokData { privacyOption PUBLIC_TO_EVERYONE, title de 90 caractères maximum, autoAddMusic true, photoCoverIndex 0 }.
   - Instagram : images `instagram/NN.jpg` (10 au maximum), providers instagram, instagramData { type POST, isAiGenerated false }. Même légende, avec « por DM » au lieu de « por mensaje ».
6. Dans `studio/plan/backlog.md`, cocher l'entrée et noter l'id Metricool et l'heure.

## Chiffres du défi

Source unique : les analytics Metricool du compte TikTok. On publie les chiffres tels quels, même petits. Jamais d'arrondi à la hausse, jamais d'estimation présentée comme un chiffre.
