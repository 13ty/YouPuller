# YouPuller

## Opis projektu

YouPuller to aplikacja umożliwiająca pobieranie i konwersję plików audio i video z serwisów takich jak YouTube. Użytkownik może wybrać format i jakość pobieranego materiału, pobierać playlisty oraz napisy z możliwością tłumaczenia i transkrypcji.

## Instalacja

### Wymagania wstępne

- System operacyjny: Linux, Windows lub WSL (Windows Subsystem for Linux)
- Połączenie z internetem

### Instalacja krok po kroku

1. Sklonuj repozytorium:

   ```
   git clone <URL_REPOZYTORIUM>
   cd Youpuller
   ```

2. Uruchom skrypt instalacyjny:
   ```
   python install.py
   ```
   Skrypt zapyta o system operacyjny i zainstaluje Minicondę lokalnie, utworzy środowisko conda oraz zainstaluje wymagane pakiety.

## Uruchomienie aplikacji

1. Po zakończeniu instalacji uruchom aplikację:

   ```
   python run.py
   ```

   Wybierz system operacyjny, a skrypt uruchomi środowisko conda i aplikację Flask.

2. Aplikacja będzie dostępna pod adresem:
   ```
   http://127.0.0.1:5000
   ```

## Funkcjonalności

- Pobieranie pojedynczych utworów i playlist
- Wybór formatu i jakości plików audio/video
- Pobieranie i tłumaczenie napisów
- Transkrypcja napisów, jeśli nie są dostępne
- Prosty interfejs webowy do obsługi aplikacji

## Roadmapa i dalszy rozwój

Szczegółowy plan rozwoju znajduje się w pliku `roadmap.md`.

## Kontakt

W razie pytań lub sugestii proszę o kontakt.
