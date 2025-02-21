import services.actions_with_movies as mov_act
import views.movie_update_delete as mud


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
                mov_act.show_movies_frm_list()
            else:
                print("Filmų sąrašas tuščias.")
        elif user_input == "4":
            print("Kol kas seansų planavimas nepasiekiamas.")
        elif user_input == "0":
            break
        else:
            print("Tokio pasirinkimo nėra. Bandykite dar kartą.")




