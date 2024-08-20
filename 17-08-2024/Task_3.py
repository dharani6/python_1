'''
### Task #3

- Explain the difference between the = operator and the == operator in Python.

- What does the ** operator do in Python, and how is it used?

- What does the ^ operator do in Python, and in what context is it commonly used?
'''

# = is assigned a variable
# == equates to True or false.
'''
Difference between = and == operators in Python
The = operator is used for assigning values to variables. For example: x = 5 assigns the value 5 to the variable x. The == operator is used for comparing if two values are equal. For example: x == 5 checks if x is equal to 5 and returns True or False.

What does the ** operator do in Python?
The ** operator is used for exponentiation in Python. It raises the number on the left to the power of the number on the right. For example: 2 ** 3 evaluates to 8 (2 raised to the power of 3) x ** 2 squares the value of x

What does the ^ operator do in Python?
The ^ operator in Python performs a bitwise XOR operation on the operands. It compares each bit of the first operand to the corresponding bit of the second operand. If both bits are different, the resulting bit is set to 1, otherwise it is set to 0. The ^ operator is commonly used in contexts like: Cryptography: For encrypting and decrypting data using XOR operations Bit manipulation: For performing operations on individual bits of a number Checking for unique elements in a list or set

XOR table:

X Y X^Y 0 0 0 0 1 1 1 0 1 1 1 0

'''
a = 5 # = is used to assign to value literal

print(a == 5) # True
print(a != 5) # False

print(" 3 * 2 = ",3*2) # single * asteric is for multiple sign
print("3**2 =", 3**2) # square of 2


lam = lambda x,y:x^y
print(lam(6,7))
