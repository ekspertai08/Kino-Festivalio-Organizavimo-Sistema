import services.actions_with_screenings as scr_act

def screening_menu():
    while True:
        print("""
Kino seansų planavimo meniu.
1. Sukurti naują kino seansą.
2. 
0. Grįžti į organizatoriaus meniu.""")
        user_input = input("Įveskite pasirinkto meniu punkto numerį: ")
        if user_input == "1":
            new = scr_act.create_screening_object()
            new.add_movie_to_screening()
            scr_act.save_sceening_to_file(new)
        elif user_input == "2":
            pass
        elif user_input == "0":
            break
        else:
            print("Tokio pasirinkimo nėra. Bandykite dar kartą.")


