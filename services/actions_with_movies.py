import os
import pickle
import models.movie as movie

def create_movie_object():
    name = input("Įveskite filmo pavadinimą: ")
    lenght = input("Įveskite filmo ilgį minutėmis: ")
    genre = input("Įveskite filmo žanrą: ")
    director = input("Įveskite filmo režisierių: ")
    release_year = input("Įveskite filmo išleidimo metus: ")
    age_rating = input("Įveskite filmo amžiaus grupę: ")
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
                result_list = [movie for movie in movie_list if getattr(movie, attributes[user_input-1]) == value]
                return result_list
            else:
                print("Tokio pasirinkimo nėra, įveskite pasirinkimo numerį 0...6 .")
        except  ValueError:
            print("Tokio pasirinkimo nėra, įveskite pasirinkimo numerį 0...6 .")
