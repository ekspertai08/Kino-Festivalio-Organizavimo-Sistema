import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from art import *
import views.first_menu

tprint("Filmu       festivalis")
while True:
    try:
        views.first_menu.first_menu()
    except Exception as e:
        print(f"{Back.RED}Nenumatyta sistemos klaida: \n{e} \nGrįžtama į programos paleidimo meniu.")
