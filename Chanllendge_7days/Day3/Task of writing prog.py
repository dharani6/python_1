#Write a Python program to calculate the area of a circle given its radius using the formula area=π×r^2 ( Take pie as 3.14)
try :
    radius = float(input("enter the values of Radius:"))
    area = 3.14*(radius**2)

    print(f"Area of a circle is {area} for a give radius {radius}")
except Exception as e:
    print(e)

'''
Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
'''
x = int(input("Enter the x Numbers"))
y = int(input("Enter the value of y Numbers"))
try:
    if x > y:
        print("x is greaater than y")
    elif x < y:
        print(f"X{x} is less than y{y}")
    elif x == y:
        print(f"x is equal to y")
    else:
        print("some this is wrong")
finally:
    print("code executed successfully")
