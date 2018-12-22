my_student ={
    'called_by_name': 'Kiana',
    'results': [70, 80, 80, 90],
    'average': None
}

class Student:
    def __init__ (self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student('Mohseni', [10, 20, 30])

print(student_one.__class__)
print(student_one.name)
print(student_one.average())


class Movie:
    def __init__(self, new_name, new_director):
        self.name = new_name
        self.director = new_director

    def credits(self):
        print('<<{}>> by {}'.format(self.name, self.director))
        return self.name

Movie('movie1', 'movie_director').credits()

"""
new_movie = Movie('movie1', 'movie_director')
print(new_movie.name)
"""
