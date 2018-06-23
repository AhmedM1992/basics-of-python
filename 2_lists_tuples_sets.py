# List (flexible)
grades_list = [40, 50, 60, 70, 80, 90]

# Tuple (immutable)
grades_tuple = (80, 90, 100, 200, 300)

# Set (unique & unordered)
grades_set = {100, 200, 400, 500, 600, 600}

print(grades_list[0])
print(grades_tuple[-1])
print(grades_set)

result = sum(grades_list) / len(grades_list)
print(result)

months = ['May', 'June', 'September']

'''Length of the word (June)'''
print(len(months[1]))

'''Quantity of items in the list'''
print(len(months))

##

'''Add items to the list'''
grades_list.append(100)
print(grades_list)

# change the value of items (assignment) in the Lists
grades_list[0] = 30
print(grades_list)

'''Add items to the Tuple'''
grades_tuple = grades_tuple + (800,)
print(grades_tuple)

grades_tuple = grades_tuple + (900, 1000)
print(grades_tuple)

'''Add items to the sets'''
grades_set.add(12)
print(grades_set)

# Sets are unordered
# grades_set[0] = 33 'ERROR' (unable to recognize which item in the set = 0)

'''Set operations'''

# Differences
my_set_1 = {1, 2, 3, 4, 5}
my_set_2 = {1, 4, 6, 7, 11, 15, 17, 20}

my_diff = my_set_2.difference(my_set_1)
print(my_diff)

print({10, 20, 30, 40}.difference({20, 30}))

# Intersections
my_intersection = my_set_1.intersection(my_set_2)
print(my_intersection)

# Union
my_union = my_set_1.union(my_set_2)
print(my_union)
