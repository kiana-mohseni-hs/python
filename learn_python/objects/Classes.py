class Movie:
    def __init__(self):
        self.movie = []

    def __len__(self):
        return len(self.movie)

    def __getitem__(self, item):
        return self.movie[item]

    def __repr__(self):
        return f'<Movie {self.movie}>'

    def __str__(self):
        return f'{self.movie}'

my_movie = Movie()
my_movie.movie.append('sound of music')
my_movie.movie.append('its a wonderful life')
print (my_movie.movie)
print (len(my_movie))
print (my_movie.movie[0])
print (my_movie.movie[1])
print (repr(my_movie))
print (my_movie)