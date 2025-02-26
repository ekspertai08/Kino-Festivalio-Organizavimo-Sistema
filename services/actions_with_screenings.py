import datetime
import pickle
import models.movie_screening_class as scr_class
import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def create_screening_object(movie):
    screening_list = open_sceenings_list_file()
    if screening_list:
        if len(screening_list)>0:
            while True:
                try:
                    screening_date_time = datetime.datetime.strptime(input("Įveskite kino seanso datą ir laiką, formatu YYYY-MM-DD, HH:MM : "), "%Y-%m-%d, %H:%M")
                    for i in screening_list:
                        if i.screening_date_time <= screening_date_time <= i.screening_end or i.screening_date_time <= screening_date_time+datetime.timedelta(minutes=int(movie.lenght)) <= i.screening_end:
                            raise IndexError
                    break
                except IndexError:
                    print(f"{Fore.RED}šiuo metu rodomas kitas kino seansas:\n{i}\n")
                except ValueError:
                    print(f"{Fore.RED}Data arba laikas, įvesta netinkamu formatu. Bandykite dar kartą.")
    else:
        while True:
            try:
                screening_date_time = datetime.datetime.strptime(input("Įveskite kino seanso datą ir laiką, formatu YYYY-MM-DD, HH:MM : "), "%Y-%m-%d, %H:%M")
                break
            except ValueError:
                print(f"{Fore.RED}Data arba laikas, įvesta netinkamu formatu. Bandykite dar kartą.")
    while True:
        try:
            aviable_seats = int(input("Įveskite maksimalų žiurovų kiekį: "))
            break
        except ValueError:
            print(f"{Fore.RED}Įvestis galima tik sveikaisiais skaičiais. Bandykite dar kartą.")

    if screening_list:
        if len(screening_list)>0:
            while True:
                try:
                    id = input("Sukurkite unikalų seanso ID: ")
                    for i in screening_list:
                        if i.id == id:
                            raise ValueError
                    break
                except ValueError:
                    print(f"{Fore.RED}Toks ID jau yra, nurodykite kitokį.")
    else:
        id = input("Sukurkite unikalų seanso ID: ")
        
    new = scr_class.Movie_screening(screening_date_time, aviable_seats, movie, id)
    return new

def open_sceenings_list_file():
    if os.path.exists("data/sceening_list_pickle"):
        with open("data/sceening_list_pickle", "rb") as file:
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

def show_screenings_list():
    screenings_list = open_sceenings_list_file()
    for num, i in enumerate(screenings_list, 1):
        print(f"{num}. {i}")

def save_updated_screening_list(screening_list):
    if open_sceenings_list_file():
        with open("data/sceening_list_pickle", "wb") as file:
            pickle.dump(screening_list, file)

def update_screening_list_after_movie_delete(old_name):
    screening_list = open_sceenings_list_file()
    if screening_list != False:
        if len(screening_list)>0:
            for num,i in enumerate(screening_list):
                if i.screening_movie != None:
                    if i.screening_movie.name == old_name:
                        number = num
                        screening_list[number].screening_movie = None
                        save_updated_screening_list(screening_list)

def update_screening_list_after_movie_update(old_name, updated_movie):
    screening_list = open_sceenings_list_file()
    if screening_list != False:
        if len(screening_list)>0:
            for num,i in enumerate(screening_list):
                if i.screening_movie != None:
                    if i.screening_movie.name == old_name:
                        number = num
                        screening_list[number].screening_movie = updated_movie
                        save_updated_screening_list(screening_list)

