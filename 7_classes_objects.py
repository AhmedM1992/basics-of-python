class PersonalInfo:
    def __init__(self):
        self.name = 'Alex'
        self.age = 25
        self.grades = (44, 55, 66)

    def total(self):
        return sum(self.grades) / len(self.grades)


student = PersonalInfo()
print(student.name)
print(student.age)
print(student.grades)
print(student.total())

# Or you can print them all
print(student.name, "is", student.age, "years old", "and his grades", student.grades)


# Example 1
class University:
    def __init__(self, name, location, rank):
        self.name = name
        self.location = location
        self.rank = rank


school_1 = University(name='MIT', location='USA', rank=1)
print(school_1.name)

school_2 = University(name='Harvard', location='USA', rank=2)
print(school_2.name)
print(school_1.name, "and", school_2.name, "are both in the", school_1.location)


# Example 2
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


first_student = Student('Rose', 'Oxford')
first_student.marks.append(44)
first_student.marks.append(55)
print(first_student.marks)
print(first_student.average())


# Example 3
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        '''Create a dictionary with keys name and price, and append that to self.items'''
        item = {'name': name, 'price': price}
        self.items.append(item)

    def stock_price(self):
        '''Add together all item prices in self.items and return the total'''
        return sum([item['price'] for item in self.items])
