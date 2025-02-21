import services.actions_with_movies as mov_act
import views.movie_choose_options as opt

def movie_update_delete_menu():
    while True:   
        print("""
        Filmų redagavimo meniu:
        1. Pašalinti filmą.
        2. Redaguoti filmą.
        0. Grįžti į organizatoriaus meniu.""")

        user_input = input("\nĮveskite pasirinkto meniu punkto numerį: ")
        if user_input == "1":
            pass
        elif user_input == "2":
            opt.movie_choose_options()

        elif user_input == "0":
            break
        else:
            print("Tokio pasirinkimo nėra. Bandykite dar kartą.")