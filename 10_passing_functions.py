def method_ception(another):
    return another()


def add_two_numbers():
    return 5 + 7


'''using a method as parameter in another method'''
print(method_ception(add_two_numbers))

'''repeating the same logic using lambda'''
print(method_ception(lambda: 5 + 7))


#Example 1: exclude 22 from the list
my_list = [22, 56, 77, 82]
print(list(filter(lambda x: x !=22, my_list)))

#OR
def not_twenty_two(x):
    return x != 22


print(list(filter(not_twenty_two, my_list)))


#OR
print([x for x in my_list if x !=22])


#Example 2: lambda vs method
(lambda x: x * 5)(6)


def same_as_lambda(x):
    return x * 5


same_as_lambda(6)
