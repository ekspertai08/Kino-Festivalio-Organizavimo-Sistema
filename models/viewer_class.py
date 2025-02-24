

class Viewer:
    def __init__(self, name):
        self.name = name
        self.rated_movies = []
        self.tickets = []

    def add_tickets(self, screening):
        self.tickets.append(screening)

