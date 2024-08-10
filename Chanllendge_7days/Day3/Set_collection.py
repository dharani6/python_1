my_set = {1,2,3,4,4,5}
my_list = [1,2,3,4,4,5]
my_tupple = (1,2,4,4,3)

print(my_set)
print(my_list)
print(my_tupple)
print(type(my_tupple))
x = 5

print(type(x))
print(type(my_set))
print(type(my_list))

try:
    string1 = "Delete"
    print(string1)
    del string1
    print(string1)

    # value assigned to variable is literals
    var = 10
    print("literal for variable var is :", var)
except Exception as e:
    print(e)


