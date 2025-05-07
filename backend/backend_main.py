S## @@ Backend Main Module

from downloader import download_video
from converter import convert_media

def process_media(url, download_path, output_format, quality, playlist=False, subtitles=False, subtitle_lang='pl'):
    """
    Główna funkcja backendu do pobierania i konwersji mediów.
    :param url: link do video lub playlisty
    :param download_path: ścieżka do zapisu pobranego pliku
    :param output_format: format docelowy pliku
    :param quality: jakość pobierania
    :param playlist: czy pobierać całą playlistę
    :param subtitles: czy pobierać napisy
    :param subtitle_lang: język napisów
    :return: ścieżka do finalnego pliku lub None w przypadku błędu
    """
    # Tutaj można rozszerzyć logikę pobierania playlist i napisów
    # Na razie przekazujemy parametry do downloadera i obsługujemy podstawowe przypadki

    # Przykładowa obsługa playlisty (do rozbudowy)
    if playlist:
        print("Pobieranie całej playlisty")
        # Można dodać obsługę playlist w downloader.py
    if subtitles:
        print(f"Pobieranie napisów w języku: {subtitle_lang}")
        # Można dodać obsługę napisów w downloader.py

    downloaded_file = download_video(url, download_path, format=output_format, quality=quality, playlist=playlist, subtitles=subtitles, subtitle_lang=subtitle_lang)
    if not downloaded_file:
        print("Pobieranie nie powiodło się.")
        return None

    if output_format not in ['mp4', 'mkv', 'avi']:
        converted_file = convert_media(downloaded_file, download_path, output_format)
        return converted_file
    else:
        return downloaded_file

if __name__ == "__main__":
    # Przykładowe wywołanie funkcji
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    output_path = "output/video.mp4"
    format = "mp4"
    quality = "best"
    result = process_media(url, output_path, format, quality)
    if result:
        print(f"Plik został zapisany: {result}")
    else:
        print("Wystąpił błąd podczas przetwarzania mediów.")
