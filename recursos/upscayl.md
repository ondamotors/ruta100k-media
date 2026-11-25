# Upscayl: la alternativa gratis a Topaz Gigapixel

Recurso gratis de RUTA 100K para seguidores. Cada dato sale de la página oficial enlazada. Verificado el 25/11/2026.

| | Topaz Gigapixel (de pago) | Upscayl (gratis) |
| --- | --- | --- |
| Precio | Plan Personal: US$149 al año, precio sin promoción | US$0, open source (AGPL-3.0) |
| Dónde funciona | Mac y PC | Windows 10+, macOS 12+ y Linux |
| El límite real | Suscripción, sin licencia perpetua | Pide tarjeta gráfica compatible con Vulkan |

## 1. Cómo tenerla gratis

- Descárgala gratis desde [upscayl.org](https://upscayl.org/) o desde la [página de versiones en GitHub](https://github.com/upscayl/upscayl/releases).
- Ojo con la Mac App Store: ahí la versión de Upscayl cuesta US$12.99 (y es la 2.11.5, más vieja). El DMG de GitHub o de su web es gratis. [Mac App Store](https://apps.apple.com/us/app/upscayl/id6468265473)
- En su web también verás Upscayl Cloud, un servicio aparte. La app de escritorio es la gratis.
- Versión actual: 2.15.0, publicada el 25 de diciembre de 2024 (Flathub la marca como de hace casi 2 años). [Notas de la versión](https://github.com/upscayl/upscayl/releases/tag/v2.15.0)

## 2. Requisitos

- Windows 10 o superior, macOS 12 o superior, o Linux.
- **Una tarjeta gráfica compatible con Vulkan.** Según el proyecto, Upscayl no funciona con la mayoría de las gráficas integradas ni solo con el procesador. Puedes revisar tu tarjeta en su [lista de compatibilidad](https://github.com/upscayl/upscayl/wiki/Compatibility-List). [README oficial](https://github.com/upscayl/upscayl)

## 3. Instalación paso a paso

**Windows**

1. Descarga el archivo `upscayl-x.x.x-win.exe` desde la página de versiones o desde upscayl.org.
2. Haz doble clic en el `.exe`.
3. Si Windows muestra el aviso de SmartScreen, toca «Más información» y luego «Ejecutar de todas formas».
4. Sigue los pasos de instalación.

**Mac**

1. Descarga el archivo `upscayl-x.x.x-mac.dmg`.
2. Ábrelo y arrastra Upscayl a Aplicaciones.
3. En Finder, entra a Aplicaciones, haz clic derecho en Upscayl y elige «Abrir». En la ventana que aparece, vuelve a tocar «Abrir».

Con Homebrew también puedes instalarla con `brew install --cask upscayl`.

**Linux**

Búscala en la tienda de tu sistema (Flathub o Snap) o descarga el AppImage, dale permiso de ejecución y ábrelo.

## 4. Ponla en español

Abre la pestaña «Settings» y, en «UPSCAYL LANGUAGE», elige español. Desde ahí, la pestaña se llama «Ajustes».

## 5. Cómo usarla

1. **Paso 1:** «Seleccionar imagen». Para una carpeta entera, activa antes «Aumento por lotes» y elige «Seleccionar carpeta».
2. **Paso 2:** «Seleccionar modelo de IA» (ver la tabla de abajo).
3. **Paso 3:** «Establecer carpeta de salida».
4. **Paso 4:** revisa el tamaño de salida que te muestra la app y pulsa el botón «Upscayl».

En «Ajustes» cambias la escala («Escala de imagen»), el formato de salida (PNG, JPG o WEBP) y, si quieres, un ancho de salida personalizado: la altura se ajusta sola y la app pide reiniciar.

**Los modelos incluidos**

| Modelo | Para qué sirve, según la app | Restricción que indica la app |
| --- | --- | --- |
| Upscayl Estándar | La mayoría de las imágenes | Ninguna |
| Upscayl Lite | La mayoría de las imágenes, más rápido, con mínima pérdida de calidad | Ninguna |
| Alta Fidelidad | Todo tipo de imágenes, con detalles realistas y texturas suaves | Ninguna |
| Arte Digital | Arte digital e ilustraciones | Ninguna |
| Remacri | Imágenes naturales, más nitidez y detalle | **No comercial** |
| Ultramix | Imágenes naturales, equilibrio entre nitidez y detalle | **No comercial** |
| Ultranítido | Imágenes naturales, con foco en la nitidez | **No comercial** |

Fuente de la tabla: los textos de la propia app en español (versión 2.15.0). [Archivo oficial](https://github.com/upscayl/upscayl/blob/v2.15.0/renderer/locales/es.json)

**Hasta cuánto agranda**

- Los modelos de IA trabajan hasta 4x. Por encima de 4x, la app solo redimensiona, sin IA.
- La excepción es «Doble Upscayl»: pasa la imagen dos veces por la IA y llega a 16x. Tarda bastante más y puede dar problemas de rendimiento en algunos equipos.

## 6. 5 usos para tu contenido

1. **Miniaturas nítidas.** Agranda una captura o un fotograma pequeño antes de usarlo como miniatura.
2. **Fotos viejas o de baja resolución.** Recupera fotos pequeñas o pixeladas para tus carruseles.
3. **Un carrusel completo de una vez.** Con «Aumento por lotes» procesas toda la carpeta del post.
4. **Ilustraciones y portadas hechas con IA.** El modelo «Arte Digital» está pensado para arte digital e ilustraciones: agranda tus imágenes generadas antes de publicarlas.
5. **Tamaño exacto para cada red.** Fija un ancho de salida personalizado y exporta en el formato que pide tu editor: PNG, JPG o WEBP.

## 7. Límites y licencia

- **Licencia:** AGPL-3.0, open source.
- **Tarjeta gráfica:** necesita una compatible con Vulkan. Con la mayoría de las integradas, o solo con el procesador, no funciona.
- **No hace milagros con el desenfoque:** mejora imágenes pequeñas o pixeladas, pero no quita el desenfoque ni corrige el foco. Para una foto fuera de foco, según el proyecto, no es la herramienta.
- **Uso comercial:** Remacri, Ultramix y Ultranítido son solo para uso no comercial. Para trabajos pagados, usa los otros modelos.
- **Versión:** la última, 2.15.0, es de diciembre de 2024.

## Lo que cuesta Topaz Gigapixel

Plan Personal: US$149 al año en pago anual, US$19 al mes con compromiso anual o US$29 al mes sin compromiso. El plan Pro cuesta US$499 al año. Es solo por suscripción: la página no ofrece licencia perpetua ni plan gratis. Al 25/11/2026 había promociones de Black Friday sin fecha de fin (Personal a US$127 el primer año, y una oferta del día a US$99 al año). [Fuente](https://www.topazlabs.com/pricing)

---

RUTA 100K · Crecer con IA, con fuentes oficiales. TikTok @ruta100k · Instagram @ruta100k.latam
