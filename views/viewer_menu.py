import services.actions_with_movies as mov_act
import services.actions_with_screenings as scr_act
import services.actions_with_viewers as vie_act
import views.ticket_reservation_menu as rs_menu
import datetime


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
                print("\nJūs turite bilietus į šiuos seansus:\n")
                screening_list = scr_act.open_sceenings_list_file()
                for num,i in enumerate(viewer.tickets, 1):
                    for a in screening_list:
                        if i == a.id:
                            print(f"{num}. {a}\n")
            else:
                print("Bilietų nėra.")
        elif user_input == "6":
            screening_list = scr_act.open_sceenings_list_file()
            to_proceed = False
            for i in viewer.tickets:
                for j in screening_list:
                    if i == j.id:
                        end = j.screening_end
                        if end < datetime.datetime.now():
                            to_proceed = True
            if to_proceed == True:
                if screening_list != False:
                    if len(screening_list)>0 and len(viewer.tickets)>0:
                        print("Peržiūrėti filmai: ")
                        for screening in screening_list:
                            for ticket in viewer.tickets:
                                if ticket == screening.id and datetime.datetime.now() > screening.screening_end:
                                    print(screening.screening_movie.name)
                                    break                                
                        movie_list = mov_act.open_movie_list_file()
                        movie_names_list = []
                        for i in movie_list:
                            movie_names_list.append(i.name)    
                        user_movie_name = input("Įveskite norimo įvertinti filmo pavadinimą: ")
                        if user_movie_name in viewer.rated_movies:
                            print("Šis filmas jau buvo įvertintas.")
                        elif user_movie_name not in movie_names_list:
                            print("Filmo pavadinimas įvestas neteisingai arba nėra tokio filmo.")
                        else:                         
                            for movie in movie_list:
                                if movie.name == user_movie_name:
                                    while True:
                                        try:
                                            user_rating = int(input("Įveskite filmo įvertinimą nuo 1 iki 10: "))
                                            if user_rating > 10:
                                                print("Įvertinimas negali būti didesnis už 10.")
                                            elif user_rating < 1:
                                                print("Įvertinimas negali būti mažesnis už 1. ")
                                            else:
                                                #update movie
                                                movie_list = mov_act.open_movie_list_file()
                                                for num,i in enumerate(movie_list):
                                                    if i.name == user_movie_name:
                                                        index_number = num
                                                movie_list[index_number].rating_list.append(int(user_rating))
                                                movie_list[index_number].rating()
                                                mov_act.save_updated_movie(movie_list)
                                                if user_movie_name not in viewer.rated_movies:
                                                    viewer.rated_movies.append(movie.name)
                                                print("Įvertinimas sėkmingas. Ačiū už įvertinimą.")
                                                break
                                        except ValueError:
                                            print("Įvestis nėra sveikasis skaičius. Mėginkite dar kartą.")

            else:
                print("Kol kas nėra peržiūrėtų filmų.")            
        elif user_input == "0":
            return viewer            
        else:
            print("Tokio pasirinkimo nėra. Bandykite dar kartą.")
