class Movie:
    def __init__(self, name, lenght, genre, director, release_year, age_rating):
        self.name = name
        self.lenght = lenght
        self.genre = genre
        self.director = director
        self.release_year = release_year
        self.age_rating = age_rating

    def __str__(self):
        return f"Pavadinimas: {self.name}, ilgis: {self.lenght} min, žanras: {self.genre}, režisierius: {self.director}, išleidimo metai: {self.release_year}, amžiaus grupė: {self.age_rating}."

    def change_movie_details(self):
        attributes = ["name", "length", "genre", "director", "release_year", "age_rating"]
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
                    setattr(self, attributes[user_input-1], new_input)
                    print("Filmo parametras sėkmingai redaguotas.")
                    break
                else:
                    print("Tokio pasirinkimo nėra, įveskite pasirinkimo numerį 0...6 .")
            except  ValueError:
                print("Tokio pasirinkimo nėra, įveskite pasirinkimo numerį 0...6 .")

