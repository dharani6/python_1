# problem to find the max between two

# Logic building formula

#1. user input -> two integers
# 2. output ->  int 1 which is greter max number it will retrun
#3. - input method

num1 = int(input("Enter the num1\n"))
num2 = int(input("Enter the num2\n"))

if num1 > num2:
    print("Number1 is greater than number2")
    print(f"Number1 {num1} is greater than number2{num2}")
else:
    print(f"Number2 {num2} is greater than number1 {num1}")