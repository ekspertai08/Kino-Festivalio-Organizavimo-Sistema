import services.actions_with_movies as mov_act
import services.actions_with_screenings as scr_act

def movie_delete():
    while True:
        if mov_act.empty_list_check():
            print("Filmo ištrynimo meniu.\n")    
            mov_act.show_movies_frm_list()
            try:
                user_input = input("\nNorėdami nutraukti ištrynimo procesą įveskite: 0\nNorėdami tęsti, įveskite norimo ištrinti filmo numerį: ")
                if user_input == "0":
                    break
                elif user_input.isnumeric():
                    user_input = int(user_input)
                    movie_list = mov_act.open_movie_list_file()
                    if user_input in range(1, len(movie_list)+1):
                        old_movie_name = movie_list[user_input-1].name
                        movie_list.pop(user_input-1)
                        mov_act.save_updated_movie(movie_list)
                        scr_act.update_screening_list_after_movie_delete(old_movie_name)
                        print("Filmas ištrintas.")
                        break
                    else:
                        print("Tokio pasirinkimo nėra. Bandykite dar kartą.")
                else:
                    raise TypeError("Įvestis galima tik skaičiais!")
            except TypeError as e:
                print(e)
            except ValueError:
                print("Pasirinkimas turi būti vienas, sveikasis skaičius!")
        else:
            print("Filmų sąrašas tuščias.")
            break

def movie_edit():
    while True:
        if mov_act.empty_list_check():
            print("Filmo redagavimo meniu.\n")
            mov_act.show_movies_frm_list()
            try:
                user_input = input("\nNorėdami nutraukti redagavimo procesą įveskite: 0\nNorėdami tęsti, įveskite norimo redaguoti filmo numerį: ")
                if user_input == "0":
                    break
                elif user_input.isnumeric():
                    user_input = int(user_input)
                    movie_list = mov_act.open_movie_list_file()
                    if user_input in range(1, len(movie_list)+1):
                        old_movie_name = movie_list[user_input-1].name
                        a = movie_list[user_input-1]
                        a.change_movie_details()
                        print(movie_list[user_input-1])
                        mov_act.save_updated_movie(movie_list)
                        scr_act.update_screening_list_after_movie_update(old_movie_name, a)
                    else:
                        print("Tokio numerio nėra.")
                else:
                    raise TypeError("Įvestis galima tik skaičiais!")
            except TypeError as e:
                print(e)
            except ValueError:
                print("Pasirinkimas turi būti vienas, sveikasis skaičius!")
        else:
            print("Filmų sąrašas tuščias.")
            break


# def movie_edit():
#     while True:
#         if mov_act.empty_list_check():
#             print("""
#             Filmo redagavimo meniu.
#             Pasirinkite ar rinksitės filmą pagal sąrašą ar pagal paiešką:
#             1. Pagal sąrašą.
#             2. Pagal paiešką.
#             0. Grįžti atgal.
# """)

#             user_input = input("\nĮveskite pasirinkto meniu punkto numerį: ")
#             if user_input == "1":
#                 mov_act.show_movies_frm_list()
#                 while True:
#                     try:
#                         user_input = input("Įveskite pasirinkto filmo numerį: ")
#                         if user_input.isnumeric():
#                             user_input = int(user_input)
#                             movie_list = mov_act.open_movie_list_file()
#                             if user_input in range(1, len(movie_list)+1):
#                                 old_movie_name = movie_list[user_input-1].name
#                                 a = movie_list[user_input-1]
#                                 a.change_movie_details()
#                                 print(movie_list[user_input-1])
#                                 mov_act.save_updated_movie(movie_list)
#                                 scr_act.update_screening_list_after_movie_update(old_movie_name, a)
#                             else:
#                                 print("Tokio numerio nėra.")
#                         else:
#                             raise TypeError("Įvestis galima tik skaičiais!")
#                     except TypeError as e:
#                         print(e)
#                     except ValueError:
#                         print("Pasirinkimas turi būti vienas, sveikasis skaičius!")

#                     break
#             elif user_input == "2":
#                 pass
#             elif user_input == "0":
#                 break
#             else:
#                 print("Tokio pasirinkimo nėra. Bandykite dar kartą.")
#         else:
#             print("Filmų sąrašas tuščias.")
#             break


# def movie_delete():
#     while True:
#         if mov_act.empty_list_check():
#             print("""
#             Filmo ištrynimo meniu.
#             Pasirinkite ar rinksitės filmą pagal sąrašą ar pagal paiešką:
#             1. Pagal sąrašą.
#             2. Pagal paiešką.
#             0. Grįžti atgal.
# """)    

#             user_input = input("\nĮveskite pasirinkto meniu punkto numerį: ")
#             if user_input == "1":
#                 mov_act.show_movies_frm_list()
#                 while True:
#                     try:
#                         user_input = input("Įveskite pasirinkto filmo numerį: ")
#                         if user_input.isnumeric():
#                             user_input = int(user_input)
#                             movie_list = mov_act.open_movie_list_file()
#                             if user_input in range(1, len(movie_list)+1):
#                                 old_movie_name = movie_list[user_input-1].name
#                                 movie_list.pop(user_input-1)
#                                 mov_act.save_updated_movie(movie_list)
#                                 scr_act.update_screening_list_after_movie_delete(old_movie_name)
#                                 print("Filmas ištrintas.")
#                                 break
#                             else:
#                                 print("Tokio pasirinkimo nėra. Bandykite dar kartą.")
#                         else:
#                             raise TypeError("Įvestis galima tik skaičiais!")
#                     except TypeError as e:
#                         print(e)
#                     except ValueError:
#                         print("Pasirinkimas turi būti vienas, sveikasis skaičius!")

#                     break
#             elif user_input == "2":
#                 pass
#             elif user_input == "0":
#                 break
#             else:
#                 print("Tokio pasirinkimo nėra. Bandykite dar kartą.")
#         else:
#             print("Filmų sąrašas tuščias.")
#             break
