Teimport subprocess

def main():
    print("Wybierz system operacyjny do uruchomienia aplikacji:")
    print("1. Linux")
    print("2. Windows")
    print("3. WSL (Windows Subsystem for Linux)")
    choice = input("Wpisz numer opcji (1/2/3): ").strip()

    if choice == '1':
        print("Uruchamianie aplikacji dla Linux...")
        subprocess.run(['bash', 'run.sh'])
    elif choice == '2':
        print("Uruchamianie aplikacji dla Windows...")
        subprocess.run(['run.bat'], shell=True)
    elif choice == '3':
        print("Uruchamianie aplikacji dla WSL...")
        subprocess.run(['bash', 'run.sh'])
    else:
        print("Nieprawidłowy wybór. Proszę uruchomić ponownie i wybrać poprawną opcję.")

if __name__ == "__main__":
    main()
