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