class film:
    def __init__(self, name, movie, actor):
        self.name = name
        self.movie = movie
        self.actor = actor
    def __str__(self):
        return  'name='+str(self.x)+ ', movie=' +str(self.y) + ', actor='+str(self.x)
    def __repr__(self):
        return { "name": self.name, "movie": self.movie, "actor": self.actor }
film1 = film("James","films(007)","James Bond")


print (film1.name,film1.movie,film1.actor)
            
first_film = film ("James","films(007)","James Bond")
