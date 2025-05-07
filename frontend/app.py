## @@ Frontend Flask App

from flask import Flask, render_template, request, redirect, url_for
import os
from backend.backend_main import process_media

app = Flask(__name__)

translations = {
    'en': {
        'title': 'YouPuller - Download audio/video',
        'url_label': 'Link to song or playlist:',
        'format_label': 'Choose format:',
        'quality_label': 'Choose quality:',
        'language_label': 'Choose language:',
        'download_button': 'Download',
        'result_prefix': 'Downloaded:'
    },
    'pl': {
        'title': 'YouPuller - Pobieranie audio/video',
        'url_label': 'Link do utworu lub playlisty:',
        'format_label': 'Wybierz format:',
        'quality_label': 'Wybierz jakość:',
        'language_label': 'Wybierz język:',
        'download_button': 'Pobierz',
        'result_prefix': 'Pobrano:'
    },
    'de': {
        'title': 'YouPuller - Audio/Video herunterladen',
        'url_label': 'Link zum Lied oder zur Wiedergabeliste:',
        'format_label': 'Format wählen:',
        'quality_label': 'Qualität wählen:',
        'language_label': 'Sprache wählen:',
        'download_button': 'Herunterladen',
        'result_prefix': 'Heruntergeladen:'
    },
    'es': {
        'title': 'YouPuller - Descargar audio/video',
        'url_label': 'Enlace a la canción o lista de reproducción:',
        'format_label': 'Elegir formato:',
        'quality_label': 'Elegir calidad:',
        'language_label': 'Elegir idioma:',
        'download_button': 'Descargar',
        'result_prefix': 'Descargado:'
    }
}

@app.route('/', methods=['GET', 'POST'])
def index():
    lang = request.form.get('language', 'pl') if request.method == 'POST' else 'pl'
    texts = translations.get(lang, translations['pl'])
    if request.method == 'POST':
        url = request.form.get('url')
        format = request.form.get('format')
        quality = request.form.get('quality')
        playlist = request.form.get('playlist') == 'yes'
        subtitles = request.form.get('subtitles') == 'yes'
        subtitle_lang = request.form.get('subtitle_lang')
        output_path = "output/downloaded_media"  # This can be improved to dynamic path or user choice
        result_path = process_media(url, output_path, format, quality, playlist=playlist, subtitles=subtitles, subtitle_lang=subtitle_lang)
        if result_path:
            result = f"{texts['result_prefix']} {result_path}"
        else:
            result = "Error processing media."
        return render_template('index.html', result=result, texts=texts, selected_lang=lang)
    return render_template('index.html', result=None, texts=texts, selected_lang=lang)

from flask import jsonify

@app.route('/debug')
def debug():
    return render_template('debug.html')

@app.route('/debug/run_test/<test_name>')
def run_test(test_name):
    if test_name == 'download':
        # Prosty test pobierania
        from backend.backend_main import process_media
        test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        output_path = "output/test_download.mp4"
        result = process_media(test_url, output_path, 'mp4', 'best')
        if result:
            return jsonify({'result': f'Test pobierania zakończony sukcesem: {result}'})
        else:
            return jsonify({'result': 'Test pobierania nie powiódł się.'})
    elif test_name == 'convert':
        # Prosty test konwersji
        from backend.converter import convert_media
        input_file = "output/test_download.mp4"
        output_file = "output/test_convert.mp3"
        result = convert_media(input_file, "output", "mp3")
        if result:
            return jsonify({'result': f'Test konwersji zakończony sukcesem: {result}'})
        else:
            return jsonify({'result': 'Test konwersji nie powiódł się.'})
    elif test_name == 'subtitles':
        # Prosty test pobierania napisów
        from backend.downloader import download_video
        test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        output_path = "output/test_subtitles.%(ext)s"
        result = download_video(test_url, output_path, format='mp4', quality='best', subtitles=True, subtitle_lang='en')
        if result:
            return jsonify({'result': f'Test pobierania napisów zakończony sukcesem: {result}'})
        else:
            return jsonify({'result': 'Test pobierania napisów nie powiódł się.'})
    else:
        return jsonify({'result': 'Nieznany test.'})

if __name__ == '__main__':
    app.run(debug=True)
