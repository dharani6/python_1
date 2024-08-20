#  Escape sequence
# This not much important but need to learn syntax error and they types if use to it then only we can solve
print("Hello World")
print("Hello \nWord") # \n is new line
print("Hello \t Word") # \t is tab

print("Hello\b Word") # \b is backspace

try:
    dir = 'c:\pramod\n.txt'
    print(dir)
    dir = "c:\pramod\n.txt"
    print(dir)
    # where this r concept will be used ?
    # Automation API , WEB autoamtion, file_path = r concept r is raw string

    dir =r"c:\pramod\n.txt"
    print(dir)
    dir =r'c:\pramod\n.txt'
    print(dir)

    #name ='pramod'nutta'
   # print(name)
    name = 'pramod\'nutta'
    print(name)

    name = "Dharani'tharan"
    print(name)
    name ="dharani'tharan"
    print(name)

except exception as e:
    print(e)


name1 = "Pramod'nutta"
print(name1)
name2 ='Pramod\'nutta'
print(name2)

#name2 =r'Pramod'nutta'
#print(name2)

name2 ='Pramod"nutta'
print(name2)