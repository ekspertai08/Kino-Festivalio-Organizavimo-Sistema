import services.actions_with_movies as mov_act
import services.actions_with_screenings as scr_act
import services.actions_with_viewers as vie_act
import views.ticket_reservation_menu as rs_menu

def viewer_menu(viewer):
    while True:
        print("""
    Žiūrovo meniu.
    1. Pamatyti filmų sąrašą.
    2. Ieškoti filmo.
    3. Pamatyti filmų seansus.
    4. Rezervuoti bilietą.
    5. Peržiūrėti rezervacijas.
    6. Žiūrėto filmo įvertinimas.
    0. Grįžti į žiūrovo autorizacijos meniu.
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
            if scr_act.empty_screenings_list_check():
                scr_act.show_screenings_list()
            else:
                print("Šiuo metu jokių kino seansų nėra..")
        elif user_input == "4":
            if scr_act.empty_screenings_list_check():
                viewer = rs_menu.ticket_reservation_menu(viewer)
            else:
                print("Šiuo metu jokių kino seansų nėra.")
        elif user_input == "5":
            if viewer.tickets:
                print("\nJūs turite rezervacijas į šiuos seansus:\n")
                screening_list = scr_act.open_sceenings_list_file()
                for i in viewer.tickets:
                    for a in screening_list:
                        if i == a.id:
                            print(f"1. {a}")
            else:
                print("Rezervuotų bilietų nėra.")
        elif user_input == "6":
            print("Kol kas nėra peržiūrėtų filmų.")            
        elif user_input == "0":
            return viewer            
        else:
            print("Tokio pasirinkimo nėra. Bandykite dar kartą.")
