'''IF statement: Simple programs'''

# Program 1
our_password = '1234aA'

user_input = input("Are you QA Engineer? (y/n)")
if user_input == 'y':
    print("The password is: " + our_password)
elif user_input == 'n':
    print("Sorry, you can't get the password")
else:
    print("Invalid input")

# Program 2
known_people = ['Mary', 'Max', 'Alex', 'Kate']

person = input("Enter the name you know: ")
if person in known_people:
    print(person + ' is in our list')
elif person not in known_people:
    print(person + ' is not in our list')

# Program 3
names = ['John', 'Antonio', 'Lorenzo']

name_input = input('Enter the person you know: ')
if name_input in names:
    print('You know {}'.format(name_input))
else:
    print("You don't know {}".format(name_input))

# Program 4
def user_menu(choice):
    if choice == "a":
        return "Add"
    elif choice == "q":
        return "Quit"

# program 5: return only even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def even_numbers():
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens

# Program 6:
def who_do_you_know():
    people = input('Enter the names of people you know, separate by comma: ')
    names_list = people.split(",")
    people_without_spaces = []
    for person in names_list:
        people_without_spaces.append(person.strip())
    return people_without_spaces


def ask_user():
    enter_name = input("Please, Enter a name: ")
    if enter_name in who_do_you_know():
        print('You know {}'.format(enter_name))


ask_user()
