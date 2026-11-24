# QA RUTA 100K, posts du 24/11/2026

8 faits revérifiés en ligne (Adobe, ElevenLabs, Descript, Upscayl, SMT, TechCrunch, Postiz).

## BLOCKER

1. **Lightroom à US$150, faux.** La [FAQ Adobe citée](https://helpx.adobe.com/lightroom/desktop/kb/lightroom-1tb-plan-faq.html), mise à jour le 17/09/2026, dit « Annual prepaid: No increase - the price will remain at US$119.88 per year » et ne contient ni « 149.99 » ni « March 20 ». La [page plans](https://www.adobe.com/products/photoshop-lightroom/plans.html) confirme US$119.88/an.
   - p1 slide 07 « US$150/año » et « Ahorro: US$150/año » → « US$120/año » et « Ahorro: US$120/año »
   - p1 slide 09 « US$150 » → « US$120 », « US$923 » → « US$893 » (somme exacte 892,76)
   - p1 slide 01 et hero de la page « US$923 » → « US$893 »
   - Page « Lightroom (1 TB): US$149.99 al año en pago anual adelantado desde el 20/03/2026. » → « Lightroom (1 TB): US$119.88 al año en pago anual adelantado. »
   - Page, barre Lightroom 54.3% → 43.5% placée sous Topaz, carte darktable après Upscayl (« Ordenadas por ahorro »).

## SHOULD FIX

2. **Premiere.** US$275.88 = US$22.99 × 12 payé au mois. Adobe propose aussi « Annual, prepaid » ([mini-plans](https://www.adobe.com/mini-plans/buy/premiere.html)), prix non affiché. Le relever au checkout. S'il est plus bas, l'utiliser et recalculer le total.

3. **Équité Descript.** Le plan Free inclut 60 min de transcription par mois ([pricing](https://www.descript.com/pricing)). Page, ajouter après le prix Descript « Su plan gratis da 1 h al mes. » Slide 09 « Ahorro total al año » → « Total de las 6 al año ».

4. **p2, Mosseri surinterprété.** [SMT, 22/01/2025](https://www.socialmediatoday.com/news/instagram-shares-algorithm-insights-2025/738034/) cite « sends are slightly more important for unconnected content ». Slide 03 « Los envíos por DM son la señal que más pesa para llegar a quien no te sigue. » → « Para llegar a quien no te sigue, los envíos por DM pesan un poco más que los likes. » Slide 02 « Pesa más para llegar » → « Pesa un poco más para llegar ».

5. **p2 slide 03.** La source parle de l'API, pas du début de la mesure. « desde diciembre de 2025 mide cuánta gente » → « desde diciembre de 2025 su API muestra cuánta gente ».

6. **p2 slide 04.** « solo » se lit « uniquement ». « puede pasar solo a tus seguidores » → « puede compartirse automáticamente con tus seguidores ». Opinion non sourcée dans un post « cero opiniones » : « Herramientas oficiales que casi nadie usa » → « Lo que Instagram recomienda usar ».

7. **p2 slides 06 et 07.** « Repostear » se confond avec le bouton Repost natif, alors que [TechCrunch](https://techcrunch.com/2026/04/30/instagram-restricts-reach-of-content-aggregators-in-new-crackdown/) vise le contenu non créé par le compte. « Repostear contenido ajeno » → « Resubir contenido ajeno », « las cuentas que repostean seguido no se recomiendan en ninguna parte de la app » → « las cuentas que suben con frecuencia contenido que no crearon dejan de recomendarse en toda la app », puce « Repostear » → « Resubir contenido ». La source de 2018 parle d'apps de croissance, pas d'achat : « Comprar seguidores o likes » → « Apps para inflar seguidores o likes », puce « Comprar seguidores » → « Inflar seguidores ».

8. **p1 slide 05, Upscayl.** Vitesse et restauration non sourcées, et la v2.15.0 du 25/12/2024 reste la dernière ([releases](https://github.com/upscayl/upscayl/releases)). « Recupera miniaturas y fotos viejas en segundos. » → « Agranda fotos y miniaturas por lotes, en tu computador. » « Necesita una tarjeta gráfica compatible con Vulkan: la mayoría de las integradas no sirven. » → « Necesita una tarjeta gráfica compatible con Vulkan, y su última versión es de diciembre de 2024. »

9. **p1 slide 06, ComfyUI.** Avec FLUX.1 (12B) et Qwen-Image (20B), le matériel compte. « Interfaz de nodos, más técnica que Midjourney. » → « Interfaz de nodos, más técnica que Midjourney, y va mejor con una buena tarjeta gráfica. »

10. **p1 slide 10.** « crecer » n'est pas transitif. « estoy creciendo esta cuenta de 0 a 100K en 60 días, en público. » → « estoy haciendo crecer esta cuenta de 0 a 100K en 60 días, a la vista de todos. » « los 6 links » → « los links de las 6 alternativas ».

11. **Visuel.** Couvertures p1 et p2, la 2e ligne du teaser touche le filet du pied (2 et 7 px). p1 slides 04 à 07 et 09, dernière ligne à 6 px du filet. Ajouter `padding-bottom: 24px` à `.body` dans brand.css. p2 slide 08, URL en 17 px illisibles sur téléphone et URL 05 coupée en plein mot (« cra / ckdown »). Dans `.sources .srcrow .u`, `word-break: break-all` → `overflow-wrap: anywhere`.

## NIT

12. p1 slide 03, « 2 GB » coupé en fin de ligne, mettre une espace insécable.
13. « plan pago » (slide 09 et page) → « plan de pago ».
14. p1 slide 04 « Y bájalo de GitHub: en la App Store de Mac » → « Descárgalo de GitHub: en la Mac App Store ».
15. p1 slide 08 et page, Postiz. [La doc](https://docs.postiz.com/providers/overview) exempte dix plateformes, « en cada red social » → « en casi todas las redes grandes ». Cap « Si facturas con tus videos » → « Si ganas dinero con tus videos ».
16. p2 slide 03 « Contenido que dan ganas de enviar » → « Contenido que da ganas de enviar ». Slide 04 « usarlas en el usuario » → « ponerlas en tu nombre de usuario », « salir en las búsquedas » → « aparecer en las búsquedas », guillemets droits → « “Estado de la cuenta” ».
17. p2 slide 05 « Pueden recomendarse hasta 3 minutos. » → « Instagram puede recomendar Reels de hasta 3 minutos. » « Úsalo » → « Úsalos ». Slide 06 « es menos probable recomendarlos » → « tienen menos probabilidades de ser recomendados ».
18. p2 slide 01 « Fuente oficial · Instagram 2026 » → « Fuente oficial · verificado en noviembre de 2026 » (sources de 2018 à 2026).

## Contrôles OK

Zéro tiret cadratin dans les deux JSON, stack.html, le template, render.py et brand.css (la puce « − » est un signe moins). Aucune légende IG trouvée pour p1 et p2, à rédiger et contrôler avant publication. 13 tactiques (3+4+2+1+3), 6 apps, compteurs, barres, licences, étoiles et versions conformes aux notes. Descript US$192 confirmé, ElevenLabs à US$6/mois en mensuel (annuel non affiché). Consentement pour le clonage de voix et filigrane mentionnés, aucune marque en logo.

**Verdict : publiable après corrections, le n°1 est bloquant.**
