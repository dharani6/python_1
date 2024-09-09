'''Task #10 -
✅ Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24
'''

def factorial(n):
    if n == 0:
        pass
    elif n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

def factor(n):
    res = 1
    for i in range(1,n+1,1):
        res = res * i
    return res

print(factor(6))
def Factorial_while():
    i =1
    fact =1
    while i <= num:
        fact = fact * i
        i = i +1
    return fact
print(F"Factorial of the given num 5 {factor(5)}")

def Sum_of_any_Num(*args):
    return sum(args)
rr = Sum_of_any_Num(1,2)
print(f"Addition of multipe args {rr}")