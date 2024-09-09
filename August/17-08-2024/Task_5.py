'''
### Task #5
- Create a program that takes two numbers as input and prints whether the first number is greater than,
less than, or equal to the second number.

'''

num1 = int(input("Enter the number1\n"))
num2 = int(input("Enter the number2\n"))

if num1 > num2:
    print(f"Number1 \'{num1}\' is greater than number2 \'{num2}\'")
if num1 < num2:
    print(f"Number1 \'{num1}\' is less than number2 \'{num2}\'")
else:
    print(f"Number1 \'{num1}\' is equal to number2 \'{num2}\'")

