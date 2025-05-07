## @@ Downloader Module

from pytube import YouTube, Playlist
from yt_dlp import YoutubeDL

def download_video(url, output_path, format='mp4', quality='best', playlist=False, subtitles=False, subtitle_lang='pl'):
    """
    Pobiera video lub audio z podanego URL.
    :param url: link do video lub playlisty
    :param output_path: ścieżka do zapisu pliku
    :param format: format pliku wyjściowego (mp4, mp3, itp.)
    :param quality: jakość do pobrania (np. 'best', 'worst', '720p')
    :param playlist: czy pobierać całą playlistę
    :param subtitles: czy pobierać napisy
    :param subtitle_lang: język napisów
    :return: ścieżka do pobranego pliku lub None
    """
    ydl_opts = {
        'format': quality,
        'outtmpl': output_path,
        'postprocessors': [],
        'writesubtitles': subtitles,
        'subtitleslangs': [subtitle_lang] if subtitles else [],
        'subtitlesformat': 'srt',
        'ignoreerrors': True,
        'quiet': True,
        'no_warnings': True,
    }

    if playlist:
        ydl_opts['yesplaylist'] = True
    else:
        ydl_opts['noplaylist'] = True

    if format in ['mp3', 'wav', 'aac', 'flac']:
        ydl_opts['postprocessors'].append({
            'key': 'FFmpegExtractAudio',
            'preferredcodec': format,
            'preferredquality': '192',
        })
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return output_path
    except Exception as e:
        print(f"Błąd podczas pobierania: {e}")
        return None
