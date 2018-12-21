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



def search_movie():
    director = movies[0]['director']
    print (movies)
    print (director)
    search_criteria = input (f'which criteria are you searching? ')
    print (search_criteria)
    search_key = input (f'which {search_criteria} are you looking for?')
    print (search_key)
    search_list = []
    print (search_list)
    search_list.append(search_key)
    print (search_list)
    results_list = []
    for i in range (len(movies)):
        if search_key == movies[i][search_criteria]:
            results_list.append(movies[i])
    print (results_list)
    return

while True:
    user_input = input ('Enter a to add a movie, l to list movies, f to find, q to quit.')
    print(user_input)
    if user_input == 'a':
        add_movie()
    elif user_input == 'f':
        search_movie()
    elif user_input == 'l':
        print('list function')
    elif user_input == 'q':
        Break
