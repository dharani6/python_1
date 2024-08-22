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
    for i in range(1,n+1):
        res = res * i
    return res

print(factor(6))


