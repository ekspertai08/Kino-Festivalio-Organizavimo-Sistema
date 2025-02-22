import services.actions_with_screenings as scr_act
import services.actions_with_movies as mov_act

def screening_menu():
    while True:
        print("""
Kino seansų planavimo meniu.
1. Sukurti naują kino seansą.
2. Peržiūrėti kino seansus.
0. Grįžti į organizatoriaus meniu.""")
        user_input = input("Įveskite pasirinkto meniu punkto numerį: ")
        if user_input == "1":
            if mov_act.empty_list_check():
                new = scr_act.create_screening_object()
                new.add_movie_to_screening()
                scr_act.save_sceening_to_file(new)
            else:
                print("Seanso sukūrimas negalimas, nes filmų sąrašas tuščias.")
        elif user_input == "2":
            if scr_act.empty_screenings_list_check():
                print()
                scr_act.show_screenings_list()
            else:
                print("Nėra sukurtų kino seansų.")
        elif user_input == "0":
            break
        else:
            print("Tokio pasirinkimo nėra. Bandykite dar kartą.")


