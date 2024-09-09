# function scope
global_b = 12  # almost work like a global varibale 

def my_function():
    a = 10 # local variable, within the function
    print(a)
    print(global_b)

def f1():
    print(global_b)
# print(a)
my_function()
print(global_b)
f1()