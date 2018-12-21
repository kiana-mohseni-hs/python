movies = [
    {
        'name': 'The alan',
        'director': 'alan',
        'year': '1994'
    },
    {
        'name': 'The blue',
        'director': 'blue',
        'year': '1994'
    },
    {
        'name': 'The tom',
        'director': 'tom',
        'year': '1994'
    },
    {
        'name': 'The tom returns',
        'director': 'tom',
        'year': '1994'
    },
    {
        'name': 'The peg',
        'director': 'peg',
        'year': '1994'
    }
]
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
    print(i)
    print (movies[i])
    if search_key == movies[i][search_criteria]:
        results_list.append(movies[i])

print (results_list)