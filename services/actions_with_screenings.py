import datetime
import pickle
import models.movie_screening_class as scr_class
import os

def create_screening_object():
    while True:
        try:
            screening_date = datetime.datetime.strptime(input("Įveskite kino seanso datą, formatu YYYY-MM-DD: "), "%Y-%m-%d")
            break
        except ValueError:
            print("Data įvesta netinkamu formatu. Bandykite dar kartą.")
    while True:
        try:
            screening_time_start = datetime.datetime.strptime(input("Įveskite kino seanso pradžios laiką, formatu HH:MM: "), "%H:%M")
            break
        except ValueError:
            print("Laikas įvestas netinkamu formatu. Bandykite dar kartą.")
    while True:
        try:
            aviable_seats = int(input("Įveskite maksimalų žiurovų kiekį: "))
            break
        except ValueError:
            print("Įvestis galima tik sveikaisiais skaičiais. Bandykite dar kartą.")
    new = scr_class.Movie_screening(screening_date, screening_time_start, aviable_seats)
    return new

def open_sceenings_list_file():
    if os.path.exists("data/sceening_list_pickle"):
        with open("data/sceening_list_pickle", "wb") as file:
            return pickle.load(file)
    else:
        return False

def save_sceening_to_file(sceening_obj):
    if open_sceenings_list_file():
        screenings_list = open_sceenings_list_file()
        screenings_list.append(sceening_obj)
        with open("data/sceening_list_pickle", "wb") as file:
            pickle.dump(screenings_list, file)
    else:
        with open("data/sceening_list_pickle", "wb") as file:
            screenings_list = []
            screenings_list.append(sceening_obj)
            pickle.dump(screenings_list, file)

def empty_screenings_list_check():
    screening_list = open_sceenings_list_file()
    if screening_list != False and len(screening_list) > 0:
        return True
    else:
        return False


# def exist_viewer_check(viewer_object):
#     viewer_list = open_viewers_list_file()
#     for i in viewer_list:
#         if i.name == viewer_object.name:
#             print("Toks žiūrovas jau egzistuoja.")
#         else:
#             save_viewer_to_list(viewer_object)
#             print("Naujas žiūrovas sukurtas, galite prisijungti.")
