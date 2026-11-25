# Chatterbox: la alternativa gratis a ElevenLabs

Recurso gratis de RUTA 100K para seguidores. Cada dato sale de la página oficial enlazada. Verificado el 25/11/2026.

| | ElevenLabs (de pago) | Chatterbox (gratis) |
| --- | --- | --- |
| Precio | Starter: US$60 al año en plan anual | US$0, open source (licencia MIT) |
| Clonar una voz | Desde el plan Starter | Sí, con unos 10 segundos de audio |
| Uso comercial | No en el plan gratis | Sí, licencia MIT |
| El límite real | Créditos por mes | La demo tiene cupo diario y cada audio lleva marca de agua |

## 1. Cómo tenerla gratis

Chatterbox es de Resemble AI. Todo es oficial y gratis:

- **Demo en español latino (es-MX), sin instalar nada:** [Chatterbox Multilingual, español de Latinoamérica](https://huggingface.co/spaces/ResembleAI/Chatterbox-Multilingual-TTS-es-mx-latam)
- **Demo multilingüe (23 idiomas):** [Chatterbox Multilingual V3](https://huggingface.co/spaces/ResembleAI/Chatterbox-Multilingual-TTS-V3)
- **Código:** [GitHub](https://github.com/resemble-ai/chatterbox) · **Modelos:** [Chatterbox](https://huggingface.co/ResembleAI/chatterbox) y [modelo de español latino](https://huggingface.co/ResembleAI/Chatterbox-Multilingual-es-mx-latam), los dos con licencia MIT.
- **Anuncio oficial:** [Resemble AI](https://www.resemble.ai/introducing-chatterbox-multilingual-open-source-tts-for-23-languages/)

## 2. Úsala en el navegador, paso a paso

1. Abre la [demo en español latino](https://huggingface.co/spaces/ResembleAI/Chatterbox-Multilingual-TTS-es-mx-latam).
2. Mejor con una cuenta gratis de Hugging Face: la demo usa GPU compartida, y tienes 5 minutos de GPU al día con cuenta gratis, contra 2 sin cuenta. [Cupos oficiales](https://huggingface.co/docs/hub/spaces-zerogpu)
3. En «Text to synthesize», pega tu texto: hasta 300 caracteres por generación. Para un guion largo, divídelo en partes.
4. En «Reference Audio File», sube un audio de la voz o grábalo con el micrófono. Con unos 10 segundos basta para clonarla. Si lo dejas vacío, usa una voz de ejemplo.
5. Ajusta «Exaggeration»: 0.5 es neutral; más alto, más expresivo. «CFG/Pace» controla el ritmo.
6. Pulsa «Generate» y descarga el audio de «Output Audio».

Consejos del equipo de Chatterbox:

- Usa un audio de referencia en el mismo idioma que el texto. Si no, la voz puede heredar el acento del audio de referencia.
- Si la persona habla rápido, baja el CFG a 0.3 aproximadamente.
- Para un tono más dramático, baja el CFG a 0.3 y sube la exageración a 0.7 o más. Subir la exageración tiende a acelerar el habla.

## 3. Instálala en tu computador

No tiene instalador: se instala con Python. El equipo la probó con Python 3.11.

1. Instala Python 3.11 desde python.org.
2. En la terminal, escribe: `pip install chatterbox-tts`
3. Crea un archivo `narrar.py` con este ejemplo (adaptado del README oficial) y ejecútalo con `python narrar.py`:

```python
import torchaudio as ta
from chatterbox.mtl_tts import ChatterboxMultilingualTTS

# "cuda" con tarjeta NVIDIA, "mps" en Mac con chip Apple, "cpu" si no tienes ninguna
modelo = ChatterboxMultilingualTTS.from_pretrained(device="cuda", t3_model="v3")

texto = "Hola, este es mi primer audio hecho con Chatterbox."
audio = modelo.generate(texto, language_id="es", audio_prompt_path="mi_voz_10s.wav")
ta.save("narracion.wav", audio, modelo.sr)
```

`mi_voz_10s.wav` es tu grabación de referencia, de unos 10 segundos. Más ejemplos en el [README](https://github.com/resemble-ai/chatterbox).

## 4. 5 usos para tu contenido

1. **Voz en off sin grabarte.** Escribe el guion de tu video o carrusel y genera la narración.
2. **Tu propia voz, sin volver a grabar.** Clona tu voz con 10 segundos de audio y genera las narraciones nuevas con ella.
3. **La misma narración en otro idioma.** El modelo multilingüe habla 23 idiomas, como inglés, portugués y francés, y puede clonar tu voz de un idioma a otro. Puede conservar tu acento.
4. **Más emoción en los momentos clave.** Sube la exageración para una apertura con más energía y bájala para una explicación tranquila.
5. **Contenido que monetizas.** La licencia MIT permite el uso comercial, algo que el plan gratis de ElevenLabs no permite.

## 5. Límites y licencia

- **Licencia:** MIT, para el código y para los modelos publicados en Hugging Face.
- **Marca de agua:** cada audio lleva la marca de agua PerTh de Resemble AI. No se oye, resiste la compresión MP3 y la edición, y se detecta con casi 100% de precisión. Tu audio será identificable como generado por IA.
- **Demo:** 300 caracteres por generación y cupo diario de GPU (5 minutos con cuenta gratis de Hugging Face, 2 sin cuenta).
- **En tu computador:** hace falta Python; no hay instalador con botones.
- **Permiso:** clona solo tu voz o la de alguien que te dio su permiso. El propio proyecto lo pide: no la uses para hacer daño.
- Versión del repositorio al 25/11/2026: Chatterbox Multilingual V3.

## Lo que cuesta ElevenLabs

El plan gratis de ElevenLabs no incluye licencia comercial y no puede usarse con fines comerciales; además, exige mencionar a ElevenLabs. [Fuente](https://elevenlabs.io/docs/help-center/legal/can-i-publish-the-content-i-generate-on-the-platform)

El plan más barato con clonación instantánea de voz y licencia comercial es Starter: US$60 al año en plan anual (US$5 al mes), o US$6 al mes en pago mensual. Hasta el 1 de diciembre, el primer mes mensual cuesta US$1. [Fuente](https://elevenlabs.io/pricing)

---

RUTA 100K · Crecer con IA, con fuentes oficiales. TikTok @ruta100k · Instagram @ruta100k.latam
