'''# Function & Types of functions in python
- A function is a reusablr set of operations.
- Block of code which can be reused.
- A function in python is a block of organized, reusable code is used to perfrom a specific task.
- Functions are defined in python using the "def" keyword, followed by the function name and parentheses ().
 . definition
 . Calling
- They may or may not return something.
- Functions can take parameters, return Values.

types of Func user defined and in build
and i user defined with arg and with key word and without arg
27-08-2024
topics covered.
decorator
lambda
List
tuple
'''

def print_arguments(*args):
    # * args = Multiple arguemnt with no limt , -> list
    # print(args[0])
    for i in args:
        print(i)

    # list = ["pramod", "amit", "Lucky"]

print_arguments("pramod", "amit", "lucky")
print_arguments("amit", "lucky")
print_arguments("amit", 10)
print_arguments("amit", 10, True)
print_arguments(("amit", 10, True, False))
print_arguments("amit", 10, True, False, "PRAMOD")


