my_list = [0, 1, 2, 3, 4]
an_equal_list = [x for x in range(5)]
print(an_equal_list)

# Examples
multiply_list = [a * 2 for a in range(2, 8)]
print(multiply_list)

divide_list = [b % 2 for b in range(10, 30)]
print(divide_list)

# list of even numbers
print([c for c in range(1, 11) if c % 2 == 0])

# Format lists
people = ["Ahmed", "John", "anna", "ALEX"]
lower_people_list = [person.strip().lower() for person in people]
print(lower_people_list)

upper_people_list = [guys.strip().upper() for guys in people]
print(upper_people_list)
