'''
LAMBDA aruguments: expression

- A lambda is an anonymous function that returns some form o data


- List
- tuple
- Map and filters


'''

#List

# list - collection of items (duplicates is allowed)
my_list = [1,2,3] # same type of data (int)


print(my_list)
print("length of the list", len(my_list))

print(my_list[0])
print(my_list[2])
my_list[0] = 'Pramod'
my_list[1] = 'dutta'
my_list[2] = "Dutta2"
#my_list[10]= "Dutta10"

print(my_list)
my_list.append(3)
print(my_list)
my_list.remove('Dutta2')
print(my_list)

