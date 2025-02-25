import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import views.coordinator_authorization as ca
import views.viewer_menu as vm
import views.viewer_authorization_menu as va

def first_menu():
    while True:
        print("""
Kino Festivalių Organizavimo Sistema
    Vartotojo tipo meniu.
              
    Pasirinkite vartotojo tipą:
    1. Organizatorius.
    2. Žiūrovas.
    0. Išjungti programą.
""")
        user_input = input("Įveskite pasirinkto meniu punkto numerį: ")
        if user_input == "1":
            ca.coordinator_authorization()
        elif user_input == "2":
            va.viewer_authorization_menu()
        elif user_input == "0":
            exit()
        else:
            print(f"{Fore.RED}Tokio pasirinkimo nėra. Bandykite dar kartą.")
