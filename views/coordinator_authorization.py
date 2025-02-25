import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import views.coordinator_menu as cm

def coordinator_authorization():
    while True:
        print("""
Organizatoriaus autentifikavimo meniu.
""")
        user_input = input("Įveskite organizatoriaus slatažodį: ")
        password = "filmas"
        if user_input == password:
            cm.coordinator_menu()
            break
        else:
            print(f"{Back.RED}Slaptažodis neteisingas. Grįžtama į vartotojo tipo meniu.")
            break