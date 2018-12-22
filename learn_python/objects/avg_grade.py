my_student = {
    'name': 'kiana mohsen' ,
    'grades': [70, 88, 90]
}

def calculate_avg (parameter):
    sum_of_grades = 0
    for i in parameter:
        sum_of_grades = (sum_of_grades + i)
    running_avg = sum_of_grades / len(parameter)
    return (running_avg)

print(my_student)
list_of_grades = my_student['grades']
avg_grade = calculate_avg (list_of_grades)
print (avg_grade)