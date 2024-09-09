square = [1,4,9,16,25]
print(square)
# list is mutable in nature
# mutable means it can change
square[3] =64
print(square)

# tuple - Collection of item
# you can't change the value
my_tuple = (1,4,9,16,25,35)
#my_tuple[4] = 44 # TypeError: 'tuple' object does not support item assignment
print(my_tuple)
my_list_tupple = list(my_tuple)
#my_tuple.__add__(1)
