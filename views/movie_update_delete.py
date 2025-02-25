import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import services.actions_with_movies as mov_act
import views.movie_edit_delete as opt

def movie_update_delete_menu():
    while True:   
        print(f"""{Fore.CYAN}
        Filmų redagavimo meniu:
        1. Pašalinti filmą.
        2. Redaguoti filmą.
        0. Grįžti į organizatoriaus meniu.""")

        user_input = input("\nĮveskite pasirinkto meniu punkto numerį: ")
        if user_input == "1":
            opt.movie_delete()
        elif user_input == "2":
            opt.movie_edit()
        elif user_input == "0":
            break
        else:
            print(f"{Fore.RED}Tokio pasirinkimo nėra. Bandykite dar kartą.")