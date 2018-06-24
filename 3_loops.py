'''FOR loop'''

a = "I love loops"

for character in a:      # iterables are strings, lists, tuples, sets and more
    print(character)

# Lists
my_list = [1, 2, 3, 4]

for number in my_list:
    print(number ** 2)

'''While loop'''

my_number = True

while my_number == True:
    print(5)
    user_input = input("Do you want to continue? (y/n)")
    if user_input == 'y':
        my_number = True
    elif user_input == 'n':
        my_number = False
    else:
        my_number = False
        print('please, Enter a valid input')
