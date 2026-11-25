# ComfyUI: la alternativa gratis a Midjourney

Recurso gratis de RUTA 100K para seguidores. Cada dato sale de la página oficial enlazada. Verificado el 25/11/2026.

| | Midjourney (de pago) | ComfyUI (gratis) |
| --- | --- | --- |
| Precio | Plan Basic: US$10 al mes, o US$96 al año en plan anual | US$0, open source (GPL-3.0) |
| Cupo | 200 minutos de GPU rápida al mes en Basic | Ninguno: corre en tu computador |
| Dónde funciona | En la nube | Windows, macOS con chip Apple y Linux |
| El límite real | Hay que pagar desde el primer mes | Más técnico, y va mejor con buena tarjeta gráfica |

## 1. Cómo tenerla gratis

- Descárgala solo desde la página oficial: [comfy.org/download](https://www.comfy.org/download). Ahí lo dicen claro: gratis y open source bajo GPL-3.0, sin funciones bloqueadas y sin periodo de prueba.
- El código está en [GitHub](https://github.com/Comfy-Org/ComfyUI). Versión del núcleo al 25/11/2026: 0.46.0, publicada el 18/11/2026.
- En la misma web verás Comfy Cloud: es otro servicio, en la nube. Para no pagar nada, usa la versión de escritorio (Comfy Desktop).

## 2. Requisitos

- **Windows:** Windows 10 o superior (x64 o ARM64). Se recomienda una tarjeta gráfica NVIDIA o AMD, pero no es obligatoria. Reserva al menos 4.85 GB de disco por instalación. [Guía oficial](https://docs.comfy.org/installation/desktop/windows)
- **Mac:** macOS 13 (Ventura) o superior, con chip Apple (M1 o más reciente). Al menos 4.85 GB de disco. [Guía oficial](https://docs.comfy.org/installation/desktop/macos)
- **Linux:** instalación manual desde GitHub.
- Suma el peso de cada modelo que descargues. Su web recomienda un disco dedicado a medida que crece tu biblioteca.

## 3. Instalación paso a paso

**En Windows**

1. Entra en [comfy.org/download](https://www.comfy.org/download): la página detecta tu sistema.
2. Abre el instalador `.exe` que descargaste y sigue los pasos.
3. Abre Comfy Desktop desde el menú Inicio o el acceso directo. La primera vez te pregunta cómo quieres ejecutarlo.

**En Mac**

1. Descarga el instalador para macOS en la misma página.
2. Abre el `.dmg` y arrastra Comfy Desktop a la carpeta Aplicaciones.
3. Ábrelo desde Launchpad o Spotlight.

## 4. Tu primera imagen con FLUX.1 [schnell]

FLUX.1 [schnell] es un modelo abierto de Black Forest Labs con licencia Apache-2.0: se puede usar con fines personales, científicos y comerciales. Genera imágenes en 1 a 4 pasos. [Ficha oficial](https://huggingface.co/black-forest-labs/FLUX.1-schnell)

1. Actualiza ComfyUI a la última versión.
2. Abre la biblioteca de plantillas (Template Library) y busca «Flux.1 Schnell». También puedes arrastrar a ComfyUI la imagen de ejemplo de la guía oficial: trae dentro el flujo y los datos de los modelos que necesita.
3. Versión ligera, la más simple: descarga el archivo `flux1-schnell-fp8.safetensors` desde la guía oficial y guárdalo en `ComfyUI/models/checkpoints/`. La guía la recomienda para equipos modestos.
4. En el nodo «Load Checkpoint», elige `flux1-schnell-fp8.safetensors`.
5. Escribe tu prompt y pulsa «Queue» (o Ctrl + Enter, Cmd + Enter en Mac).

La versión completa usa 4 archivos (`clip_l`, `t5xxl_fp8_e4m3fn`, `ae` y `flux1-schnell`), cada uno en su carpeta, y pide más memoria de video. Todo el detalle: [guía oficial de FLUX.1 en ComfyUI](https://docs.comfy.org/tutorials/flux/flux-1-text-to-image).

## 5. Bonus: texto dentro de la imagen con Qwen-Image

Qwen-Image es un modelo abierto de 20B parámetros, con licencia Apache-2.0, fuerte para escribir texto dentro de la imagen y para editar (cambiar el estilo, agregar o quitar objetos). En ComfyUI, busca «Qwen-Image» en la biblioteca de plantillas. [Ficha oficial](https://huggingface.co/Qwen/Qwen-Image) · [Guía en ComfyUI](https://docs.comfy.org/tutorials/image/qwen/qwen-image)

Ojo: es pesado. En la prueba oficial, con una RTX 4090D de 24 GB, usó el 86% de la memoria de video y tardó entre 34 y 94 segundos por imagen según la versión.

## 6. 5 usos para tu contenido

1. **Portadas y miniaturas.** Genera la escena o el fondo con FLUX.1 [schnell] y pon tu texto encima en tu editor de siempre.
2. **Trabajos para clientes o contenido que monetizas.** FLUX.1 [schnell] y Qwen-Image tienen licencia Apache-2.0, que permite el uso comercial.
3. **Muchas versiones de la misma idea.** Prueba 20 portadas distintas sin gastar ningún cupo mensual: el único límite es tu computador.
4. **Repetir un estilo que funcionó.** Arrastra a ComfyUI una imagen hecha con ComfyUI y recuperas el flujo completo que la creó, semilla incluida.
5. **Video y música en el mismo programa.** ComfyUI trae plantillas para modelos abiertos de video, como Wan 2.2, y de música, como ACE-Step 1.5. [Lista oficial](https://github.com/Comfy-Org/ComfyUI)

Truco: el modo App convierte un flujo en un formulario simple, con solo los campos que eliges (el prompt, la imagen de salida). Así no tocas los nodos cada vez. [Guía del modo App](https://docs.comfy.org/interface/app-mode)

## 7. Límites y licencia

- ComfyUI tiene licencia GPL-3.0. Cada modelo tiene la suya: FLUX.1 [schnell] y Qwen-Image son Apache-2.0, pero FLUX.1 [dev] es solo para uso no comercial. Revisa la licencia de cada modelo antes de un trabajo pagado.
- Trabajas con nodos conectados: es más técnico que escribir un prompt en Midjourney.
- Funciona sin tarjeta gráfica dedicada, pero su web la recomienda con fuerza: con más memoria de video, modelos más grandes.
- En Mac, solo con chip Apple.
- Los nodos de API, que dan acceso a modelos cerrados, son de pago y opcionales. Los modelos abiertos que corren en tu computador no cuestan nada.
- Una vez instalado, funciona sin internet.

## Lo que cuesta Midjourney

La página de planes de Midjourney no incluye plan gratis ni periodo de prueba. El más barato, Basic, cuesta US$10 al mes, o US$96 al año (US$8 al mes) con el plan anual, e incluye 200 minutos de GPU rápida al mes. El modo Relax ilimitado empieza en Standard, a US$30 al mes. [Fuente](https://docs.midjourney.com/docs/plans)

---

RUTA 100K · Crecer con IA, con fuentes oficiales. TikTok @ruta100k · Instagram @ruta100k.latam
