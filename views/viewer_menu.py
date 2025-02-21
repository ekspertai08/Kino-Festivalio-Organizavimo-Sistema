import services.actions_with_movies as mov_act

def viewer_menu():
    while True:
        print("""
    Žiūrovo meniu.
    1. Pamatyti filmų sąrašą.
    2. Ieškoti filmo.
    3. Rezervuoti bilietą.
    4. Žiūrėto filmo įvertinimas.
    0. Grįžti į vartotojo tipo meniu.
""")
        user_input = input("\nĮveskite pasirinkto meniu punkto numerį: ")
        if user_input == "1":
            if mov_act.empty_list_check():
                mov_act.show_movies_frm_list()
            else:
                print("Filmų sąrašas tuščias.")
        elif user_input == "2":
            if mov_act.empty_list_check():
                result = mov_act.search_movies()
                if len(result) == 0:
                    print("Nieko nerasta.")
                else:
                    print("Rasta:")
                    for num, i in enumerate(result, 1):
                        print(f"{num}. {i}")   
            else:
                print("Filmų sąrašas tuščias.")
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        elif user_input == "0":
            break
        else:
            print("Tokio pasirinkimo nėra. Bandykite dar kartą.")
