class Viewer:
    def __init__(self, name):
        self.name = name
        self.watched_movies = []
        self.tickets = []

    def add_tickets(self, screening):
        self.tickets.append(screening)

