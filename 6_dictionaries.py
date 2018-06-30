my_dic = {'name': 'Ahmed', 'age': 25, 'position': 'QA'}
student = {'name': 'John', 'class': 6, 'grades': [50, 70, 80]}
evens_dict = {1: 4, 2: 6, 3: 8}

universities = [
    {
        'name': 'MIT',
        'location': 'US'
    },
    {
        'name': 'Oxford',
        'location': 'UK'
    }
]

print(student['grades'])
print(my_dic['age'])
print(sum(student['grades']))

# Change value in dictionary
student['name'] = 'Rose'
print(student)


# Example 1: count the average grade
def grades_average(data):
    grades = data['grades']
    return sum(grades) / len(grades)


# Example 2: calculate the average grade of the class
def class_average(stduent_list):
    total = 0
    count = 0
    for student in stduent_list:
        total = sum(stduent_list['grades'])
        count = len(stduent_list['grades'])
    return total / count


