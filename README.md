# 📥 YT Downloader — Linux

Un script de línea de comandos para descargar videos y audio de YouTube (y [muchos sitios más](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)) usando la libreria `yt-dlp`.

La idea de este script es poder hacer llamadas a la API de YouTube para descargar tanto videos como solamente el audio de los mismos desde una linea de comandos, sin tener que depender de páginas de dudosa procedencia con toneladas de anuncios molestos.

---

## Features

- 🎬 **Descarga video** en la mejor calidad disponible (MP4)
- 🎵 **Extrae audio** en MP3 con calidad máxima
- 📁 **Rutas dinámicas** — guarda en `~/Downloads/yt-dlp/` sin importar quién lo use ni en qué máquina
- 🔍 **Auto-instalación** de `yt-dlp` si no está presente
- ⚠️ **Detección de ffmpeg** con instrucciones claras si falta

---

## 📋 Requisitos

- Python 3.7+
- `ffmpeg` instalado en el sistema
- `yt-dlp` (el script lo instala automáticamente si no está)

### Instalar ffmpeg

```bash
# Ubuntu / Debian
sudo apt install ffmpeg

# Arch / Manjaro
sudo pacman -S ffmpeg

# Fedora
sudo dnf install ffmpeg

# openSUSE
sudo zypper install ffmpeg
```

---

## Uso

```bash
python YT_Downloader.py
```

Se va a mostrar un menú interactivo:

```
==================================================
  VIDEO/AUDIO DOWNLOADER  (Linux)
==================================================
  📁 Videos → /home/user/Downloads/yt-dlp/Video
  🎵 Audios → /home/user/Downloads/yt-dlp/Audio
==================================================

1) Descargar Video
2) Descargar Solo Audio (MP3)
3) Salir
```
---

## 📂 Rutas de guardado de las descargas por defecto

| Tipo   | Ruta                                  |
|--------|---------------------------------------|
| Video  | `~/Downloads/yt-dlp/Video/`           |
| Audio  | `~/Downloads/yt-dlp/Audio/`           |

Las carpetas se crean automáticamente si no existen.

---

## 🌐 Sitios soportados

Cualquier sitio que soporte `yt-dlp`: YouTube, SoundCloud, Twitter/X, Vimeo, TikTok, Twitch y [cientos más](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md).

---

## Buscás la versión para Windows?

Este repo fue una adaptación del script que hice para Windows, si lo necesitas la versión original para Windows está **[acá.](https://github.com/Vuadens/Video-downloader-with-YT-DLP)**

---

## 📄 Licencia

MIT 
