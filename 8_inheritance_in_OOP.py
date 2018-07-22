class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    def friend(self, friend_name):
        return Student(friend_name, self.school)


class WorkingStudent(Student):
    def __init__(self, name, school, position, salary):
        Student.__init__(self, name, school)
        self.salary = salary
        self.position = position


Alex = WorkingStudent("Alex", "MIT", "QA", 3000)
print(Alex.position)


# Example 1
class StudentAddress(WorkingStudent):
    def __init__(self, name, school, position, salary, country, city, street):
        WorkingStudent.__init__(self, name, school, position, salary)
        self.country = country
        self.city = city
        self.street = street


Anna = StudentAddress("Anna", "Oxford",
                      "Programmer", 2000,
                      "USA", "LA", "My street")
print(Anna.country)
print(Anna.city)

