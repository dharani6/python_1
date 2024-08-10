name = 'Dharani'
try:
    print(len(name))
    for i in range(len(name+1)):
        print(i)
        print(name[i])
except Exception as e:
        print(e)


import keyword

print(keyword.kwlist)