'''Task #11 -
✅ Fibonaci series 0,0+1, 0+1+1, n = 7 0, 1, 2, 3, 5, 8, 13

'''
'''
def fibonoci(num):
    res =[]
    ans = 0
    for i in range(num):
        ans = res[i] + res[i-1]
        res.append(ans)
    return res

print(fibonoci(7)) '''
fib = 7


def fibo(n):
    n1, n2 = 0, 1
    fib_list = []

    for i in range(n):
        nth = n1 + n2
        n1 = n2
        n2 = nth
        fib_list.append(nth)
        print(nth)

    print(fib_list)
fibo(7)
