import services.actions_with_movies as mov_act

class Movie_screening:
    def __init__(self, screening_date, screening_time_start, avialable_seats):
        self.screening_date = screening_date
        self.screening_time_start = screening_time_start
        self.screening_movies = []
        self.avialable_seats = avialable_seats

    def add_movie_to_screening(self):
        if mov_act.empty_list_check:
            mov_act.show_movies_frm_list()
            movies_list = mov_act.open_movie_list_file()
            while True:
                user_input = input("Įveskite filmų eilės numerius, kurios norite pridėti prie šio kino seanso(numerius atskirkite kableliu su tarpu arba tiesiog tarpu): ").replace(",","").split()
                try:
                    for u in user_input:
                        u = int(u)
                        if u < 1 or u > len(movies_list):
                            raise IndexError
                        self.screening_movies.append(movies_list[u-1])
                        print("Filmai pridėti i šį kino seansą.")
                        break
                    break
                except ValueError:
                    print(f"{u} nėra eilės skaičius. Bandykite dar kartą.")
                except IndexError:
                    print(f"'{u}' nėra tokio filmo numerio. Bandykite dar kartą.")
        else:
            print("Filmų sąrašas tuščias.")

