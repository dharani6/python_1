'''
### Task #6

- Develop a Python script that calculates the square and cube of a given number.

'''
num1 = float(input("Enter the number for opeartion of SQ and cubie !!!\n"))

def CubieAndSquare(num):
    cubie = num*num*num
    square = num*num
    print((cubie,square))

CubieAndSquare(num1)

cubie = lambda num:num**3
square = lambda num:num**2

print(cubie(num1),square(num1))

#Task from You tube
#you have 5 box finnd the unique 1 of them its arranged in 4,4,5,3,3
# solutiion
lst = [4,4,5,3,3]

for i in lst:
    if lst.count(i) == 1:
        print(f"Unique No in the give list is {i}")