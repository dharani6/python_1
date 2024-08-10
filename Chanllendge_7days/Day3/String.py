name = 'Dharanitharan.R'
for i in range(len(name)):
    print(name[i],'-',i, end=" ")
print(name)
print(len(name))
print(name[0])
print(name[5])
print(name[6])

#functions of string

print(name.lower())
print(name.capitalize())
print(name.casefold())
print('DHARNAI'.casefold())
print(name.index('t'))
print("count of 'a' in name",name.count('a'))
try:
    str = "Dharani"
    str[0] ='A' # Not possible
except Exception as e:
    print("Exception is :",e)


    #Slicing
# for slicing var[start,end,step]
my_str = " I am learning python from the TheTestingAcademy"
print(my_str[0:4])
print(my_str[8:len(my_str)])