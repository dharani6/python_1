#decorators
# Understanding Decorators in python

'''
Decorator in python are a way to modify the behavior of a function or class without changing its source code.

They are a powerful tool that allows you yo wrap another function and extend its fucnitionality
while keeping the original functions code unchanged


'''


def my_decorator(func):

    # two parts what is the wrapp and call

    def wrapper():
        print("1.somthing before the function is callsed :")
        print("2.add Helmet, dashcash, glove, kee gard")
        func()
        print("3.something is happing after the function is called.")
    return wrapper()
@my_decorator
def drive_bike():
    print("4.i am driving")

#drive_bike()
@my_decorator
def driving_scooty():
    print("driving scooty")

