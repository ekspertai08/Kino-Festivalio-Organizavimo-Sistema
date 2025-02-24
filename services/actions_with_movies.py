import os
import pickle
import models.movie as movie
import datetime

def create_movie_object():
    movie_list = open_movie_list_file()
    while True:
        try:
            name = input("Įveskite filmo pavadinimą: ")
            if name == "":
                raise ValueError("Filmo pavadinimo įvestis negali būti tuščia. Bandykite dar kartą.")
            if empty_list_check():
                for i in movie_list:
                    if i.name == name:
                        raise ValueError("Filmas tokiu pavadinimu jau yra. Bandykite dar kartą.")
            break
        except ValueError as e:
            print(e)
    while True:
        lenght = input("Įveskite filmo ilgį minutėmis: ")
        try:
            if lenght == "":
                raise KeyError("Filmo trukmės įvestis negali būti tuščia. Bandykite dar kartą.")        
            lenght = int(lenght)
            if lenght <= 0:
                raise KeyError("Filmo trukmė negali būti mažesnė už 0, ar lygi 0.")
            break
        except KeyError as e:
            print(e)
        except ValueError:
            print("Filmo ilgį galima įvesti tik sveikaisiais skaičiais. Bandykite dar kartą.")
    genre = input("Įveskite filmo žanrą: ")
    director = input("Įveskite filmo režisierių: ")
    while True:
        release_year = input("Įveskite filmo išleidimo metus: ")
        try:
            release_year = int(release_year)
            if release_year > int(datetime.datetime.now().year):
                print("Filmo išleidimo data negali būti atetyje. Bandykite dar kartą.")
            elif release_year < 1888:
                print("Filmo išleidimo data negali būti ankstesnė, nei pirmo pasaulyje išleisto filmo. Bandykite dar kartą.\n(PS pirmas filmas išleistas 1888 metais)")
            else:
                break
        except ValueError:
            print("Filmo išleidimo metai, gali būti įvesti tik sveikaisiais skaičiais. Bandykite dar kartą.")
    age_ratings = ["V", "N-7", "N-13", "N-16", "N-18"]
    while True:
        age_rating = input("Įveskite filmo amžiaus grupę: ")
        if age_rating not in age_ratings:
            print("Įvesta neteisinga amžiaus grupė. Galimos amžiaus grupės yra: V, N-7, N-13, N-16, N-18.\nBandykite dar kartą.")
        else:
            break
    return movie.Movie(name, lenght, genre, director, release_year, age_rating)

def open_movie_list_file():
    if os.path.exists("data/movie_list.pickle"):
        with open("data/movie_list.pickle", "rb") as file:
            return pickle.load(file)
    else:
        return False

def save_updated_movie(updated_list):
    with open("data/movie_list.pickle", "wb") as file:
        pickle.dump(updated_list, file)


def save_movie_to_list(movie):
    if open_movie_list_file():
        movie_list = open_movie_list_file()
        movie_list.append(movie)
        with open("data/movie_list.pickle", "wb") as file:
            pickle.dump(movie_list, file)
    else:
        with open("data/movie_list.pickle", "wb") as file:
            movie_list = []
            movie_list.append(movie)
            pickle.dump(movie_list, file)

def show_movies_frm_list():
    if open_movie_list_file():
        movie_list = open_movie_list_file()
        for num, i in enumerate(movie_list, 1):
            print(f"\t{num}. {i}")

def select_movie(number):
    if open_movie_list_file():
        movie_list = open_movie_list_file()
        return movie_list[number]
    else:
        print("Filmų sąrašas tuščias.")

def empty_list_check():
    movie_list = open_movie_list_file()
    if movie_list != False and len(movie_list) > 0:
        return True
    else:
        return False
    
def search_movies():
    movie_list = open_movie_list_file()
    attributes = ["name", "lenght", "genre", "director", "release_year", "age_rating"]
    while True:
        print("""Galimi paieškos parametro pasirinkimai:
                  1. Pavadinimas.
                  2. Ilgis.
                  3. Žanras.
                  4. Režisierius.
                  5. Išleidimo metai.
                  6. Amžiaus grupė.
                  0. Grįžti.""")
        user_input = input("Paieškos parametro numerį: ")
        if user_input == "0":
            break
        try:
            user_input = int(user_input)
            if user_input in range(1, 7):
                value = input("Įveskite ieškomą vertę: ")
                if value.isnumeric():
                    value = float(value)
                result_list = [movie for movie in movie_list if getattr(movie, attributes[user_input-1]) == value]
                return result_list
            else:
                print("Tokio pasirinkimo nėra, įveskite pasirinkimo numerį 0...6 .")
        except  ValueError:
            print("Tokio pasirinkimo nėra, įveskite pasirinkimo numerį 0...6 .")
