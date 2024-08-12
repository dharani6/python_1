def factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return factorial(num) * factorial(num-1)

#print(factorial(6))

# # Factorial
# n = 5
# 5*4*3*2*1 = 120
# n = 3
# 3*2*! => 6

number = int(input("Enter the number\n"))

fact = 1
if number < 0:
    print("Factorial")
elif number == 0:
    print("Fact - ", 1)
else:
    fact = 1
    for i in range(1, number + 1):
        fact = fact * i

print("Fact ->>", fact)