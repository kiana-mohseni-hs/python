"""
Enter a to add a movie, l to list movies, f to find, q to quit.

"""
movies = [
    {
        'name': 'The alan',
        'director': 'alan',
        'year': '1994'
    },
    {
        'name': 'The blue',
        'director': 'blue',
        'year': '1997'
    },
    {
        'name': 'The tom',
        'director': 'tom',
        'year': '1996'
    },
    {
        'name': 'The tom returns',
        'director': 'tom',
        'year': '1995'
    },
    {
        'name': 'The peg',
        'director': 'peg',
        'year': '1994'
    }
]

def add_movie():
    name = input ('enter movie name: ')
    director = input ('enter movie director:')
    date = input ('enter movie date')
    movies.append({'name':name, 'director':director,'date':date})
    print (movies)
    return

def movie_finder(search_property, search_value):
    found = []
    for movie in movies:
        if movie[search_property] == search_value:
            found.append(movie)
    return (found)

def search_movie():
    search_property = input (f'which property are you searching by? ')
    search_key = input (f'which {search_property} are you looking for?')
    movie_list = movie_finder(search_property, search_key)
    print (movie_list)
    return

user_input = ''
while user_input != 'q':
    user_input = input ('Enter a to add a movie, l to list movies, f to find, q to quit.')
    print(user_input)
    if user_input == 'a':
        add_movie()
    elif user_input == 'f':
        search_movie()
    elif user_input == 'l':
        print('list function')

