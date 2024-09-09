# functions with argument and name
def greet():
    print("hello, there!!")


def greet_by_name(name): # name is called parameters or argument
    print("hello,", name)

greet_by_name("Dharani")
greet_by_name(123)
greet_by_name(123)
greet_by_name(True)
greet_by_name(3.14)

result = greet_by_name("Pramod")
greet_by_name(greet())