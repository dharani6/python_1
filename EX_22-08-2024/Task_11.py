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
N = 7
fib =[0 for i in range(N)]
print(fib)