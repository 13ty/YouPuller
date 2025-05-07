## @@ Converter Module

import ffmpeg

def convert_media(input_path, output_path, format):
    """
    Konwertuje plik multimedialny do wybranego formatu.
    :param input_path: ścieżka do pliku wejściowego
    :param output_path: ścieżka do pliku wyjściowego
    :param format: format docelowy (np. mp3, mp4, wav)
    :return: ścieżka do przekonwertowanego pliku
    """
    try:
        stream = ffmpeg.input(input_path)
        stream = ffmpeg.output(stream, output_path, format=format)
        ffmpeg.run(stream, overwrite_output=True)
        return output_path
    except ffmpeg.Error as e:
        print(f"Błąd podczas konwersji: {e}")
        return None
