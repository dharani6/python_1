# method to convert string to list

str = "Hello we are going to convert string to list via different ways"

# using list key word
#list_str = list(str)
#print(list_str)
# print output['H', 'e', 'l', 'l', 'o', ' ', 'w', 'e', ' ', 'a', 'r', 'e', ' ', 'g', 'o', 'i', 'n', 'g', ' ', 't', 'o', ' ', 'c', 'o', 'n', 'v', 'e', 'r', 't', ' ', 's', 't', 'r', 'i', 'n', 'g', ' ', 't', 'o', ' ', 'l', 'i', 's', 't', ' ', 'v', 'i', 'a', ' ', 'd', 'i', 'f', 'f', 'e', 'r', 'e', 'n', 't', ' ', 'w', 'a', 'y', 's']

# using split function
str_split_fun = str.split(' ')
#str_split_fun1 = str.split('') # ValueError: empty separator  str_split_fun1 = str.split('') # ValueError: empty separator
#print(str_split_fun) #['Hello', 'we', 'are', 'going', 'to', 'convert', 'string', 'to', 'list', 'via', 'different', 'ways']
#print(str_split_fun1) #
# list comprention
Comp_list = [char for char in str]
#print(Comp_list) # output ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'e', ' ', 'a', 'r', 'e', ' ', 'g', 'o', 'i', 'n', 'g', ' ', 't', 'o', ' ', 'c', 'o', 'n', 'v', 'e', 'r', 't', ' ', 's', 't', 'r', 'i', 'n', 'g', ' ', 't', 'o', ' ', 'l', 'i', 's', 't', ' ', 'v', 'i', 'a', ' ', 'd', 'i', 'f', 'f', 'e', 'r', 'e', 'n', 't', ' ', 'w', 'a', 'y', 's']

#print(list(map(list,str))) # output [['H'], ['e'], ['l'], ['l'], ['o'], [' '], ['w'], ['e'], [' '], ['a'], ['r'], ['e'], [' '], ['g'], ['o'], ['i'], ['n'], ['g'], [' '], ['t'], ['o'], [' '], ['c'], ['o'], ['n'], ['v'], ['e'], ['r'], ['t'], [' '], ['s'], ['t'], ['r'], ['i'], ['n'], ['g'], [' '], ['t'], ['o'], [' '], ['l'], ['i'], ['s'], ['t'], [' '], ['v'], ['i'], ['a'], [' '], ['d'], ['i'], ['f'], ['f'], ['e'], ['r'], ['e'], ['n'], ['t'], [' '], ['w'], ['a'], ['y'], ['s']]
#print(list(map(list,str_split_fun))) # output [['H', 'e', 'l', 'l', 'o'], ['w', 'e'], ['a', 'r', 'e'], ['g', 'o', 'i', 'n', 'g'], ['t', 'o'], ['c', 'o', 'n', 'v', 'e', 'r', 't'], ['s', 't', 'r', 'i', 'n', 'g'], ['t', 'o'], ['l', 'i', 's', 't'], ['v', 'i', 'a'], ['d', 'i', 'f', 'f', 'e', 'r', 'e', 'n', 't'], ['w', 'a', 'y', 's']]

# convert the list to string
print(f"List of words {str_split_fun} before convertion")
new_string = ' '.join(str_split_fun) # Using join method
print(new_string)

new_string1 = ''
for word in str_split_fun: # use for loop and new variable
    new_string1 = new_string1 + ' ' + word
print(new_string1)

