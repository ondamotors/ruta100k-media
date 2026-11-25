# ACE-Step: la alternativa gratis a Suno

Recurso gratis de RUTA 100K para seguidores. Cada dato sale de la página oficial enlazada. Verificado el 25/11/2026.

| | Suno (de pago) | ACE-Step 1.5 (gratis) |
| --- | --- | --- |
| Precio | Pro: US$10 al mes, o US$96 al año en plan anual | US$0, open source (licencia MIT) |
| Plan gratis | 50 créditos al día, sin derechos comerciales ni descargas | No hace falta: corre en tu computador |
| Uso comercial | Desde el plan Pro | Permitido, según su ficha oficial |
| El límite real | Pagar para descargar y usar tus canciones | Tarjeta NVIDIA o Mac con chip Apple, y unos 10 GB de disco |

## 1. Cómo tenerla gratis

- **Código y paquetes:** [GitHub de ACE-Step 1.5](https://github.com/ace-step/ACE-Step-1.5), licencia MIT.
- **Ficha del modelo:** [Hugging Face](https://huggingface.co/ACE-Step/Ace-Step1.5). Dice que puedes usar la música generada con fines comerciales y que el modelo se entrenó con música con licencia, música libre de derechos y datos sintéticos.
- **Demo en el navegador:** [Space oficial en Hugging Face](https://huggingface.co/spaces/ACE-Step/Ace-Step-v1.5). Usa GPU compartida: con cuenta gratis de Hugging Face tienes 5 minutos de GPU al día. [Cupos](https://huggingface.co/docs/hub/spaces-zerogpu)
- El README también enlaza acemusic.ai, un servicio en línea. Su página de precios muestra un plan gratis con límites (4 canciones al día, sin descargas ni uso comercial) y una nota que dice que con ACE-Step v1.5 no hay límites. Como sus condiciones no son claras, esta guía usa la versión en tu computador.

## 2. Requisitos

- **Windows:** tarjeta gráfica NVIDIA. El paquete portable requiere CUDA 12.8.
- **Mac:** chip Apple (M1, M2, M3 o M4).
- **Disco:** unos 10 GB para los modelos principales, que se descargan la primera vez.
- **Memoria de video:** según su equipo, corre con menos de 4 GB. Con 6 GB o menos, el asistente que escribe la descripción y la letra (modelo de lenguaje) viene apagado: escribes tú el estilo y la letra.
- Solo con el procesador también funciona, pero mucho más lento.

La duración máxima depende de tu tarjeta: 6 minutos con 4 GB o menos, y entre 8 y 10 minutos con más memoria. [Guía de compatibilidad](https://github.com/ace-step/ACE-Step-1.5/blob/main/docs/en/GPU_COMPATIBILITY.md)

## 3. Instalación paso a paso

**Windows (NVIDIA)**

1. Descarga el paquete portable [ACE-Step-1.5.7z](https://files.acemusic.ai/acemusic/win/ACE-Step-1.5.7z), enlazado en el README oficial. Ya trae Python y todas las dependencias.
2. Descomprímelo con un programa que abra archivos `.7z`.
3. Abre `start_gradio_ui.bat`.
4. La primera vez descarga los modelos. Cuando termine, abre `http://localhost:7860` en tu navegador.

**Mac (chip Apple)**

1. Descarga el paquete portable [ACE-Step-1.5.zip](https://files.acemusic.ai/acemusic/mac/ACE-Step-1.5.zip) y descomprímelo.
2. Abre la Terminal en esa carpeta y escribe, solo la primera vez: `chmod +x start_gradio_ui_macos.sh`
3. Luego: `./start_gradio_ui_macos.sh`
4. Abre `http://localhost:7860` en tu navegador.

Instalación avanzada en cualquier sistema (con uv) y guía completa: [INSTALL](https://github.com/ace-step/ACE-Step-1.5/blob/main/docs/en/INSTALL.md).

## 4. Tu primera canción

1. Arriba, en «Settings», pulsa «Initialize Service». El cuadro de estado te dice qué nivel de tarjeta detectó y la duración máxima.
2. **Si tienes más de 6 GB de memoria de video, usa el modo Simple:** elige «Simple», describe la canción en «Song Description» (por ejemplo, «lo-fi tranquilo con piano para estudiar»), elige el idioma de la voz, pulsa «Create Sample» y después «Generate Music».
3. **Con cualquier tarjeta, usa el modo Custom:** elige «Custom», escribe el estilo en «Caption» y tu letra en «Lyrics», fija la duración y pulsa «Generate Music».
4. ¿Sin voz? Marca la casilla «Instrumental».
5. Escucha y descarga el resultado desde el reproductor. Por defecto sale en MP3; también puedes elegir WAV o FLAC.

Para ordenar la letra, usa etiquetas de estructura como `[Intro]`, `[Verse]`, `[Chorus]`, `[Bridge]` y `[Outro]`. Y cuida que el estilo y la letra digan lo mismo: si se contradicen, el resultado empeora. [Tutorial oficial](https://github.com/ace-step/ACE-Step-1.5/blob/main/docs/en/Tutorial.md)

## 5. 5 usos para tu contenido

1. **Música de fondo propia.** Genera la pista de tus videos en el estilo que quieras, de 10 segundos a 10 minutos según tu tarjeta.
2. **El jingle de tu marca o de tu serie.** Escribe tu propia letra: acepta más de 50 idiomas, español incluido.
3. **Una base instrumental para tu voz en off.** Marca «Instrumental» y pon tu narración encima.
4. **Arreglar sin empezar de cero.** El modo Repaint regenera solo el tramo que no te gustó y deja el resto igual. También sirve para alargar la canción.
5. **Otra versión de una canción tuya.** El modo Remix cambia el estilo de un audio que subes y mantiene su estructura melódica.

Truco avanzado: puedes entrenar un LoRA con tu propio estilo a partir de unas pocas canciones. El proyecto habla de 8 canciones y 1 hora de entrenamiento en una RTX 3090.

## 6. Límites y licencia

- **Licencia:** MIT. Su ficha en Hugging Face permite el uso comercial de la música generada.
- **Parecidos involuntarios:** su propio equipo advierte que una canción generada puede infringir derechos sin querer por parecerse a otra. Recomienda revisar que sea original, decir que usaste IA y pedir permiso si imitas un estilo protegido.
- **Equipo:** el paquete de Windows pide NVIDIA; el de Mac, chip Apple. Solo con el procesador va mucho más lento.
- **Disco:** unos 10 GB.
- **Demo en línea:** cupo diario de GPU.

## Lo que cuesta Suno

- **Free:** US$0, 50 créditos al día, sin derechos comerciales, sin descargas mensuales y sin separación de pistas.
- **Pro:** US$10 al mes, o US$8 al mes facturado anual (US$96 al año). 2500 créditos al mes, derechos comerciales y 20 descargas al mes.
- **Premier:** US$30 al mes, o US$24 al mes facturado anual (US$288 al año). 10 000 créditos al mes y 60 descargas al mes.

Al 25/11/2026 la página mostraba además una promoción de Black Friday en planes anuales. [Fuente](https://suno.com/pricing)

---

RUTA 100K · Crecer con IA, con fuentes oficiales. TikTok @ruta100k · Instagram @ruta100k.latam
