'''Reverse the given number
n = int(input("enter the number:"))
rev = 0
while n>0:
    r = n%10
    rev = rev * 10 + r
    n = n//10
print(rev)

'''
'''
num = 54331
rev_num = int(str(num)[::-1])
print (rev_num)
'''
'''
def Power(N,R):
    power_num = pow(N,R)
    return power_num //(10**9 +7)
'''
'''
def firstdigit(num):
    while num>=10:
        num = num//10
    return print(num)
'''
