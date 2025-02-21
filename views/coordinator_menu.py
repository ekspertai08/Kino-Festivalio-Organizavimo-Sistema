import services.actions_with_movies as mov_act
import views.movie_update_delete as mud


def coordinator_menu():
    while True:
        print("""
    Organizatoriaus meniu:
    1. Pridėti naują filmą.
    2. Pašalinti arba antaujinti esamą filmą.
    3. Filmų peržiūra ir paieška.
    4. Seansų planavimas.
    0. Grįžti į pradinį meniu.""")
        user_input = input("\nĮveskite pasirinkto meniu punkto numerį: ")
        if user_input == "1":
            new_movie = mov_act.create_movie_object()
            mov_act.save_movie_to_list(new_movie)
            print("Filmas pridėtas.")
        elif user_input == "2":
            mud.movie_update_delete_menu()
        elif user_input == "3":
            mov_act.show_movies_frm_list()
        elif user_input == "4":
            pass
        elif user_input == "0":
            break
        else:
            print("Tokio pasirinkimo nėra. Bandykite dar kartą.")




