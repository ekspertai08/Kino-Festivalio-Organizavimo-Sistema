import services.actions_with_movies as mov_act
import datetime

class Movie:
    def __init__(self, name, lenght, genre, director, release_year, age_rating):
        self.name = name
        self.lenght = lenght
        self.genre = genre
        self.director = director
        self.release_year = release_year
        self.age_rating = age_rating
        self.rating_list = []
        self.rating = self.rating()

    def __str__(self):
        return f"Pavadinimas: {self.name}, ilgis: {self.lenght} min, žanras: {self.genre}, režisierius: {self.director}, išleidimo metai: {self.release_year}, amžiaus grupė: {self.age_rating}, įvertinimų reitingas: {self.rating}"
    
    def __repr__(self):
        return f"Pavadinimas: {self.name}"

    def rating(self):
        if len(self.rating_list) == 0:
            return f"Įvertinimų dar nėra"
        else:
            return round(sum(self.rating_list)/len(self.rating_list), ndigits=1)

    def change_movie_details(self):
        attributes = ["name", "lenght", "genre", "director", "release_year", "age_rating"]
        while True:
            print("""Galimi filmo parametrų redagavimo pasirinkimai:
                  1. Pavadinimas.
                  2. Ilgis.
                  3. Žanras.
                  4. Režisierius.
                  5. Išleidimo metai.
                  6. Amžiaus grupė.
                  0. Grįžti.""")
            user_input = input("Įveskite norimo redaguoti parametro numerį: ")
            if user_input == "0":
                break
            try:
                user_input = int(user_input)
                if user_input in range(1, 7):
                    new_input = input("Įveskite naują reikšmę: ")
                    if user_input == 1:
                        if new_input == "":
                            print("Filmo pavadinimas, negali būti tuščias.")
                            continue
                        else:
                            movie_list = mov_act.open_movie_list_file()
                            if movie_list != False:
                                if len(movie_list)>0:
                                    for i in movie_list:
                                        if i.name == new_input:
                                            raise KeyError("Filmas tokiu pavadinimu jau yra.")
                    elif user_input == 2:
                        while True:
                            try:
                                new_input = int(new_input)
                                if new_input <= 0:
                                    print("Filmo ilgis negali būti 0 ar mažiau už 0.")
                                    new_input = input("Įveskite naują reikšmę: ")
                                else:
                                    break
                            except ValueError:
                                print("Filmo ilgio įvedimas galimas tik sveikaisiais skaičiais.")
                                new_input = input("Įveskite naują reikšmę: ")
                    elif user_input == 5:
                        while True:
                            try:
                                new_input = int(new_input)
                                if new_input > int(datetime.datetime.now().year):
                                    print("Filmo išleidimo data negali būti atetyje. Bandykite dar kartą.")
                                    new_input = input("Įveskite naują reikšmę: ")
                                elif new_input < 1888:
                                    print("Filmo išleidimo data negali būti ankstesnė, nei pirmo pasaulyje išleisto filmo. Bandykite dar kartą.\n(PS pirmas filmas išleistas 1888 metais)")
                                    new_input = input("Įveskite naują reikšmę: ")
                                else:
                                    break
                            except ValueError:
                                print("Filmo išleidimo metai, gali būti įvesti tik sveikaisiais skaičiais. Bandykite dar kartą.")
                                new_input = input("Įveskite naują reikšmę: ")
                    setattr(self, attributes[user_input-1], new_input)
                    print("Filmo parametras sėkmingai redaguotas.")
                    break
                else:
                    print("Tokio pasirinkimo nėra, įveskite pasirinkimo numerį 0...6 .")
            except KeyError as e:
                print(e)
            except  ValueError:
                print("Tokio pasirinkimo nėra, įveskite pasirinkimo numerį 0...6 .")
