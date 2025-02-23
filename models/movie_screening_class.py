import services.actions_with_movies as mov_act
import datetime

class Movie_screening:
    def __init__(self, screening_date_time, avialable_seats, screening_movie):
        self.screening_date_time = screening_date_time
        self.screening_movie = screening_movie
        self.screening_end = screening_date_time + datetime.timedelta(minutes=int(screening_movie.lenght))
        self.avialable_seats = avialable_seats

    def __str__(self):
        return f"Seanso pradžios data ir laikas: {self.screening_date_time}\nSeanso pabaigos data ir laikas: {self.screening_end}\nLaisvų vietų kiekis: {self.avialable_seats}\nSeanso rodomas filmas: \t{self.screening_movie.name}"
    
    # def screening_time_end(self):
    #     if len(self.screening_movies) == 0:
    #         return f"Dar nesuplatuota"
    #     else:
    #         self.screening_end = self.screening_date_time + datetime.timedelta(minutes=int(self.screening_movies[0].lenght))
    #         return self.screening_end

    # def add_movie_to_screening(self):
    #     if mov_act.empty_list_check:
    #         mov_act.show_movies_frm_list()
    #         movies_list = mov_act.open_movie_list_file()
    #         while True:
    #             user_input = input("Įveskite filmo numerį, kurio seansą norite suplanuoti: ")
    #             try:
    #                 user_input = int(user_input)
    #                 if user_input > 0 and user_input <= len(movies_list):
    #                     self.screening_movies.append(movies_list[user_input-1])
    #                     self.screening_end = self.screening_time_end()
    #                     print("Seansas suplanuotas.")
    #                     break
    #                 else:
    #                     raise IndexError
    #             except ValueError:
    #                 print(f"{user_input} nėra skaičius. Bandykite dar kartą.")
    #             except IndexError:
    #                 print(f"'{user_input}' nėra tokio filmo numerio. Bandykite dar kartą.")
    #     else:
    #         print("Filmų sąrašas tuščias.")

