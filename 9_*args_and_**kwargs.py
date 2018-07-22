#Examples of methods with arguments
def my_method(arg1, arg2):
    return arg1 + arg2


my_method(7, 8)


def long_method(arg1, arg2, arg3, arg4, arg5):
    return arg1 + arg2 + arg3 + arg4 + arg5


long_method(3, 4, 5, 6, 7)


#Usage of *args (for arguments without names)
def simple_method(*args):
    return sum(args)


simple_method(10, 20, 30, 40, 50, 60)


def student(*args):
    return args


print(student("Rose", "MIT", "software developer", "4th stage"))


#Usage of kwargs (for named arguments)
def employee(**kwargs):
    return kwargs


print(employee(name="Ahmed", position="QA Engineer", company="ABC"))
