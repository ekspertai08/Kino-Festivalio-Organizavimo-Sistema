import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import views.coordinator_menu as cm

def coordinator_authorization():
    while True:
        print("""
Organizatoriaus autentifikavimo meniu.
""")
        user_name = input("Įveskite organizatoriaus vardą: ")
        name = "Mantas"
        password = "filmas"
        user_password = input("Įveskite organizatoriaus slatažodį: ")

        if user_name == name and user_password == password:
            print(f"{Fore.GREEN} Prisijungta sėkmingai.")
            cm.coordinator_menu()
            break
        else:
            print(f"{Back.RED}Organizatoriaus vardas arba slaptažodis neteisingas. Grįžtama į vartotojo tipo meniu.")
            break