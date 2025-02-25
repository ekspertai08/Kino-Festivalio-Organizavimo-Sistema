import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import services.actions_with_movies as mov_act
import views.movie_update_delete as mud
import views.screening_menu as scr_menu


def coordinator_menu():
    while True:
        print("""
    Organizatoriaus meniu:
    1. Pridėti naują filmą.
    2. Pašalinti arba atnaujinti esamą filmą.
    3. Filmų peržiūra ir paieška.
    4. Seansų planavimas.
    0. Grįžti į pradinį meniu.""")
        user_input = input("\nĮveskite pasirinkto meniu punkto numerį: ")
        if user_input == "1":
            new_movie = mov_act.create_movie_object()
            mov_act.save_movie_to_list(new_movie)
            print("Filmas pridėtas.")
        elif user_input == "2":
            if mov_act.empty_list_check():
                mud.movie_update_delete_menu()
            else:
                print("Filmų sąrašas tuščias.")
        elif user_input == "3":
            if mov_act.empty_list_check():
                print("""
            Filmo rodymo ir paieškos meniu.
            Pasirinkite ar rinksitės filmą pagal sąrašą ar pagal paiešką:
            1. Parodyti filmų sąrašą.
            2. Ieškoti filmo.
            0. Grįžti atgal.
""")
                user_input = input("\nĮveskite pasirinkto meniu punkto numerį: ")
                if user_input == "1":
                    mov_act.show_movies_frm_list()
                elif user_input == "2":
                    result = mov_act.search_movies()
                    if result == None:
                        continue
                    else:
                        if len(result) == 0:
                            print("Nieko nerasta.")
                        else:
                            print("Rasta:")
                            for num, i in enumerate(result, 1):
                                print(f"{num}. {i}")   
            else:
                print("Filmų sąrašas tuščias.")
        elif user_input == "4":
            scr_menu.screening_menu()
        elif user_input == "0":
            break
        else:
            print(f"{Fore.RED}Tokio pasirinkimo nėra. Bandykite dar kartą.")




