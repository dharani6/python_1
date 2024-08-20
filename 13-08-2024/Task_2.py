'''
Task #2

Create a program , take 2 inputs from the user num1, num2 and give them
max
pow num1 to num2
sub, mul, sum, div.
Format your out with f{""}
'''
num1 = int(input("Emter Number 1\n"))
num2 = int(input("Emter Number 2\n"))

print(f"The max of the give 2 number is {max(num1,num2)}")

# if loop condition
def max_num(num1,num2):
    print("executed from if loop condition start")
    if num1 > num2:
        print(f"Amoung the give number{num1} is greater")
    else:
        print(f"Amoung the give number{num2} is greater")
    print("executed from if loop condition end")
max_num(num1,num2)

print(f"the power num1 over num2 is {pow(num1,num2)}")
print(f"the power num2 over num1 is {pow(num2,num1)}")
def Power_of_num(num1,num2):
    return num1 ** num2
print(f"fromthe give number power facotr is {Power_of_num(num1,num2)}")

def calculation(num1,num2):
    print(f"addition of 2 number is {num1+num2}")
    print(f"subtract of 2 number is {num1 - num2}")
    print(f"multipication of 2 number is {num1 * num2}")
    print(f"division of 2 number is {num1 // num2}")
calculation(num1,num2)