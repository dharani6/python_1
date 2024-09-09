class Calculatore:
    def add(self, num1, num2):
        return num1 + num2
    def subtract(self, num1, num2):
        return num1 - num2
    def multiple(self, num1, num2):
        return num1 * num2
    def divide(self, num1, num2):
        return num1 // num2

calculator = Calculatore()
print(calculator.add(2, 1), calculator.subtract(5, 4), calculator.multiple(66, 5), calculator.divide(5, 2))
'''try:'''
num1 = int(input("Enter Number 1"))
num2 = int(input("Enter Number 2"))
operations = ["add", "subtract", "multiple", "divide"]
for operation in operations:
    if operation == "add":
        sum = calculator.add(num1, num2)
        print(f"Sum of the number1 and number2 is {sum}")
    elif operation == "subtract":
        sub = calculator.subtract(num1, num2)
        print(f"difference of number1 and number2 is {sub}")
    elif operation == "multiple":
        multiple = calculator.multiple(num1, num2)
        print(f"multiplication of number1 and number 2 is {multiple}")
    elif operation == "divide":
        divide = calculator.divide(num1, num2)
        print(f"division of number1 and number 2 is {divide}")
# except Exception as e:
#   print(e)

