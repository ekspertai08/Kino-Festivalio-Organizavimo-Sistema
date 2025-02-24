import services.actions_with_movies as mov_act
import datetime

class Movie_screening:
    def __init__(self, screening_date_time, avialable_seats, screening_movie, id):
        self.screening_date_time = screening_date_time
        self.screening_movie = screening_movie
        self.screening_end = screening_date_time + datetime.timedelta(minutes=int(screening_movie.lenght))
        self.avialable_seats = avialable_seats
        self.id = id

    def __str__(self):
        return f"Seanso pradžios data ir laikas: {self.screening_date_time}\nSeanso pabaigos data ir laikas: {self.screening_end}\nLaisvų vietų kiekis: {self.avialable_seats}\nSeanso rodomas filmas: \t{self.screening_movie_if()}"
    
    def screening_movie_if(self):
        if self.screening_movie == None:
            return f"Nėra priskirto filmo"
        else:
            return self.screening_movie.name

