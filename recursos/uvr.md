# Ultimate Vocal Remover (UVR): la alternativa gratis a Lalal.ai

Recurso gratis de RUTA 100K para seguidores. Cada dato sale de la página oficial enlazada. Verificado el 25/11/2026.

| | Lalal.ai (de pago) | Ultimate Vocal Remover (gratis) |
| --- | --- | --- |
| Precio | Lite: US$7.5 al mes, o US$90 al año | US$0, open source (código con licencia MIT) |
| Plan gratis | 10 minutos en la cola lenta, para probar | No hace falta: corre en tu computador |
| Dónde funciona | En la nube | Windows 10+, macOS Big Sur+ y Linux |
| El límite real | Minutos por mes | Para ir rápido pide tarjeta gráfica, y su versión estable es de 2023 |

## 1. Cómo tenerla gratis

- Página oficial: [GitHub de Ultimate Vocal Remover](https://github.com/Anjok07/ultimatevocalremovergui). El código de la app tiene licencia MIT.
- Descargas de la versión 5.6: [página de la versión](https://github.com/Anjok07/ultimatevocalremovergui/releases/tag/v5.6).
- Los instaladores ya traen la interfaz, Python, PyTorch y todo lo necesario: no tienes que instalar nada antes.

## 2. Requisitos

- **Windows:** Windows 10 o superior, de 64 bits. Hay que instalarla en el disco principal, C (en otro disco, según el proyecto, queda inestable). En procesadores Intel Pentium y Celeron no está garantizada.
- **Mac:** macOS Big Sur o superior, con chip Apple (M1) o Intel. En Mac antiguos o de gama baja no está garantizada.
- **Linux:** instalación manual (instrucciones para Debian y Arch en el README).
- **Tarjeta gráfica:** para procesar con la tarjeta, una NVIDIA GTX 1060 de 6 GB como mínimo; recomiendan 8 GB. Con AMD Radeon el soporte es limitado: en Windows, prueba la versión DirectML (beta) para AMD Radeon o Intel Arc. En Mac con chip M1, la aceleración funciona con Demucs v4 y con todos los modelos MDX-Net.
- El tiempo de cada separación depende mucho de tu equipo: los modelos son exigentes.

## 3. Instalación paso a paso

**Windows**

1. Descarga [UVR_v5.6.0_setup.exe](https://github.com/Anjok07/ultimatevocalremovergui/releases/download/v5.6/UVR_v5.6.0_setup.exe).
2. Instálalo en el disco C, el principal.
3. ¿Tarjeta AMD Radeon o Intel Arc? Prueba la [versión DirectML](https://github.com/Anjok07/ultimatevocalremovergui/releases/download/v5.6/UVR_1_15_25_22_30_BETA_full.exe).

**Mac**

1. Descarga el DMG de tu Mac: [chip Apple (arm64)](https://github.com/Anjok07/ultimatevocalremovergui/releases/download/v5.6/Ultimate_Vocal_Remover_v5_6_MacOS_arm64.dmg) o [Intel (x86_64)](https://github.com/Anjok07/ultimatevocalremovergui/releases/download/v5.6/Ultimate_Vocal_Remover_v5_6_MacOS_x86_64.dmg).
2. Instálalo. La primera vez puede tardar de 5 a 10 minutos en abrir, según tu Mac.
3. Si no abre, sigue la sección «MacOS Users: Having Trouble Opening UVR?» del [README](https://github.com/Anjok07/ultimatevocalremovergui).

## 4. Cómo usarla

1. **«Select Input»:** elige el archivo de audio, o varios a la vez.
2. **«Select Output»:** elige la carpeta donde se guardan los resultados.
3. Elige el formato de salida: WAV, FLAC o MP3.
4. **«CHOOSE PROCESS METHOD»:** VR Architecture, MDX-Net, Demucs o Ensemble Mode (combina varios modelos para un mejor resultado). Después, elige el modelo.
5. Si tienes una NVIDIA compatible, marca **«GPU Conversion»**.
6. ¿Solo quieres un archivo? Marca «Vocals Only» (solo la voz) o «Instrumental Only» (solo la música).
7. Pulsa **«Start Processing»**.

Más modelos: el botón de ajustes, a la izquierda de «Start Processing», abre los ajustes y el «Download Center».

Si aparece un error de memoria, baja el valor de «Segment» o de «Window»: es la solución que da el proyecto.

## 5. 5 usos para tu contenido

1. **Voz e instrumental por separado.** De una canción o de un audio sacas dos archivos: la voz sola y la música sola.
2. **Rescatar un video grabado con música de fondo.** Exporta el audio de tu video, sepáralo, quédate con las voces y pon en tu editor una música que puedas usar.
3. **Una voz sin eco.** Con el modelo VR «UVR-DeEcho-DeReverb» instalado, la app quita la reverberación de una pista de voz.
4. **4 pistas para tus remixes.** Con los modelos Demucs de 4 pistas separas voz, batería, bajo y el resto.
5. **Varios audios de una vez.** En «Select Input» eliges todos los archivos del proyecto y los procesas en una sola tanda.

## 6. Límites y licencia

- **Licencia:** el código de la app es MIT. Los desarrolladores de UVR entrenaron todos los modelos del paquete, salvo los modelos Demucs v3 y v4 de 4 pistas. Si usas sus modelos en otra app, piden dar crédito a UVR.
- **Versión:** la estable es la 5.6, de 2023. Después salieron versiones beta.
- **Velocidad:** depende de tu equipo. Sin una tarjeta compatible, ten paciencia.
- **Derechos:** separar una canción no te da derechos sobre ella. Si no es tuya, úsala solo con permiso o con licencia.

## Lo que cuesta Lalal.ai

- **Starter:** gratis, 10 minutos en la cola lenta. Según Lalal.ai, sirve para probar el servicio antes de pagar.
- **Lite:** US$7.5 al mes, o US$90 al año, con 90 minutos al mes en la cola rápida.
- **Pro:** US$15 al mes, o US$180 al año, con 250 minutos al mes en la cola rápida.

[Fuente](https://www.lalal.ai/pricing/)

---

RUTA 100K · Crecer con IA, con fuentes oficiales. TikTok @ruta100k · Instagram @ruta100k.latam
