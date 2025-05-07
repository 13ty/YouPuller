Swiimport os
import platform
import subprocess

def main():
    print("Wybierz system operacyjny do instalacji:")
    print("1. Linux")
    print("2. Windows")
    print("3. WSL (Windows Subsystem for Linux)")
    choice = input("Wpisz numer opcji (1/2/3): ").strip()

    if choice == '1':
        print("Uruchamianie instalacji dla Linux...")
        subprocess.run(['bash', 'install.sh'])
    elif choice == '2':
        print("Uruchamianie instalacji dla Windows...")
        subprocess.run(['install.bat'], shell=True)
    elif choice == '3':
        print("Uruchamianie instalacji dla WSL...")
        subprocess.run(['bash', 'install.sh'])
    else:
        print("Nieprawidłowy wybór. Proszę uruchomić ponownie i wybrać poprawną opcję.")

if __name__ == "__main__":
    main()
