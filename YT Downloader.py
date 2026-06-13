import os
import subprocess
import sys
from pathlib import Path

# Dynamic paths — work for any user on any Linux system
BASE_PATH = Path.home() / "Downloads" / "yt-dlp"
AUDIO_PATH = BASE_PATH / "Audio"
VIDEO_PATH = BASE_PATH / "Video"


def cls():
    os.system("clear")


def check_dependency(name):
    """Check if a CLI tool is available in PATH"""
    try:
        subprocess.run([name, "--version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def check_yt_dlp():
    """Check if yt-dlp is installed"""
    return check_dependency("yt-dlp")


def check_ffmpeg():
    """Check if ffmpeg is installed"""
    return check_dependency("ffmpeg")


def install_yt_dlp():
    """Install yt-dlp using pip"""
    print("\nyt-dlp no está instalado. Instalando...")
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--user", "yt-dlp"],
            check=True,
        )
        cls()
        print("yt-dlp instalado correctamente!")
        return True
    except subprocess.CalledProcessError:
        cls()
        print("Error al instalar yt-dlp. Instalá manualmente con: pip install yt-dlp")
        return False



def warn_ffmpeg():
    """Print ffmpeg installation instructions for common Linux distros"""
    print("\n⚠  ffmpeg no está instalado. Es necesario para convertir audio/video.")
    print("   Instalalo con el gestor de paquetes de tu distro:")
    print("     Ubuntu/Debian:  sudo apt install ffmpeg")
    print("     Arch/Manjaro:   sudo pacman -S ffmpeg")
    print("     Fedora:         sudo dnf install ffmpeg")
    print("     openSUSE:       sudo zypper install ffmpeg\n")


def create_directories():
    """Create download directories if they don't exist"""
    AUDIO_PATH.mkdir(parents=True, exist_ok=True)
    VIDEO_PATH.mkdir(parents=True, exist_ok=True)


def download_video(url):
    """Download video with best quality"""
    print(f"\nDescargando video: {url}")
    print(f"Destino: {VIDEO_PATH}")

    command = [
        "yt-dlp",
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "--merge-output-format", "mp4",
        "--recode-video", "mp4",
        "-o", str(VIDEO_PATH / "%(title)s.%(ext)s"),
        url,
    ]

    try:
        subprocess.run(command, check=True)
        cls()
        print("\n✓ Video descargado correctamente!")
    except subprocess.CalledProcessError:
        print("\n✗ Error al descargar el video. Verificá la URL e intentá de nuevo.")


def download_audio(url):
    """Download audio only in MP3 format"""
    print(f"\nDescargando audio: {url}")
    print(f"Destino: {AUDIO_PATH}")

    command = [
        "yt-dlp",
        "-f", "bestaudio/best",
        "-x",
        "--audio-format", "mp3",
        "--audio-quality", "0",
        "-o", str(AUDIO_PATH / "%(title)s.%(ext)s"),
        url,
    ]

    try:
        subprocess.run(command, check=True)
        print("\n✓ Audio descargado correctamente!")
    except subprocess.CalledProcessError:
        print("\n✗ Error al descargar el audio. Verificá la URL e intentá de nuevo.")


def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 50)
    print("  VIDEO/AUDIO DOWNLOADER  (Linux)")
    print("=" * 50)
    print(f"  📁 Videos → {VIDEO_PATH}")
    print(f"  🎵 Audios → {AUDIO_PATH}")
    print("=" * 50)
    print("\n1) Descargar Video")
    print("2) Descargar Solo Audio (MP3)")
    print("3) Salir")
    print("\n" + "=" * 50)


def main():
    """Main program loop"""
    # Check dependencies
    if not check_yt_dlp():
        if not install_yt_dlp():
            return

    if not check_ffmpeg():
        warn_ffmpeg()
        input("Presioná Enter para continuar de todas formas (algunas funciones pueden fallar)...")
        cls()

    # Create download directories
    create_directories()

    while True:
        display_menu()
        choice = input("\nElegí una opción (1-3): ").strip()

        if choice == "1":
            url = input("\nIngresá la URL del video: ").strip()
            if url:
                download_video(url)
            else:
                print("Error: la URL no puede estar vacía.")

        elif choice == "2":
            url = input("\nIngresá la URL del video: ").strip()
            if url:
                download_audio(url)
            else:
                cls()
                print("Error: la URL no puede estar vacía.")

        elif choice == "3":
            print("\nHasta la próxima!")
            break

        else:
            print("\nOpción inválida. Ingresá 1, 2 o 3.")

        input("\nPresioná Enter para continuar...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        cls()
        print("\n\nDe nada pa")
        sys.exit(0)