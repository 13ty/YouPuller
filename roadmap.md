# Roadmap projektu aplikacji do pobierania i konwersji audio/video

## 1. Przygotowanie środowiska i konfiguracja projektu

- [ ] Utworzenie repozytorium projektu
- [ ] Konfiguracja środowiska Python (wirtualne środowisko, wymagane biblioteki)
- [ ] Przygotowanie struktury katalogów (backend, frontend, gui)

## 2. Backend

- [x] Implementacja modułu pobierania multimediów z serwisów (YouTube, itp.) z wykorzystaniem bibliotek takich jak pytube lub yt-dlp
  - Tag w kodzie: ## @@ Downloader Module (backend/downloader.py)
- [x] Implementacja modułu konwersji plików multimedialnych z użyciem ffmpeg
  - Tag w kodzie: ## @@ Converter Module (backend/converter.py)
- [x] Obsługa wyboru formatu i jakości pobieranych plików
- [x] Obsługa pobierania pojedynczych utworów i playlist
- [x] Logowanie i obsługa błędów
- [x] Główny moduł integrujący funkcjonalności backendu
  - Tag w kodzie: ## @@ Backend Main Module (backend/backend_main.py)

## 3. Frontend / GUI

- [x] Projekt i implementacja interfejsu użytkownika
  - [ ] GUI desktopowe (np. Tkinter, PyQt) lub
  - [x] Webowy frontend (np. Flask + HTML/CSS/JS)
- [x] Formularz do wprowadzania linku i wyboru parametrów (format, jakość)
- [x] Wyświetlanie postępu pobierania i konwersji
- [x] Informacje o zakończeniu procesu i lokalizacji plików
- [x] Dodanie obsługi pobierania playlist i napisów w UI

## 7. Obsługa napisów do filmów

- [ ] Pobieranie napisów w wybranym języku z serwisów (np. YouTube)
- [ ] Tłumaczenie napisów, jeśli nie są dostępne w wybranym języku
- [ ] Transkrypcja napisów za pomocą bibliotek Pythona, jeśli napisy nie są dostępne
- [ ] Przygotowanie miejsca w GUI na wybór i obsługę napisów
- [ ] Uwzględnienie funkcjonalności napisów przy wyborze bibliotek backendowych

## 4. Integracja

- [x] Połączenie frontend-u z backend-em (np. API REST lub bezpośrednie wywołania funkcji)
- [x] Testowanie przepływu danych i funkcjonalności

## 5. Testowanie i optymalizacja

- [ ] Testy funkcjonalne i integracyjne
- [ ] Optymalizacja wydajności i obsługi błędów
- [ ] Dokumentacja użytkownika i dewelopera

## 6. Dodatkowe funkcje (opcjonalne)

- [ ] Pobieranie metadanych i zapisywanie ich w plikach
- [ ] Harmonogram pobierania
- [ ] Obsługa dodatkowych serwisów
- [ ] Integracja z bazą danych do zarządzania plikami

## 7. Obsługa napisów do filmów

- [ ] Pobieranie napisów w wybranym języku z serwisów (np. YouTube)
- [ ] Tłumaczenie napisów, jeśli nie są dostępne w wybranym języku
- [ ] Transkrypcja napisów za pomocą bibliotek Pythona, jeśli napisy nie są dostępne
- [ ] Przygotowanie miejsca w GUI na wybór i obsługę napisów
- [ ] Uwzględnienie funkcjonalności napisów przy wyborze bibliotek backendowych

---

# Postęp prac

- [ ] Roadmap utworzona
- [ ] Backend - w trakcie / do rozpoczęcia
- [ ] Frontend/GUI - w trakcie / do rozpoczęcia
- [ ] Integracja - w trakcie / do rozpoczęcia
- [ ] Testowanie - w trakcie / do rozpoczęcia
