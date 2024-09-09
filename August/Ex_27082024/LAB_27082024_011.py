# lambda expression
# a lambda is an anynomous function that return some form of data.

def triple_me(num):
    return num**3

O = triple_me(10)
print(O)

# lambda expression basicall says 1 line of code that you want to return

OO = lambda num: num ** 3

print(OO(10))

def add_10(n):
    return n+10
print(add_10(10))
A = lambda n: n+ 10
print(A((9)))

AA = lambda a,b,c: a+ b + c
print(AA(2,3,4))



