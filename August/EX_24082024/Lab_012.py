# function with more argumments and defaullt

def Multiple_args(name1="Arpitha", name2="pramod", name3 = "Amit"):
    print("Multiple args",name1,name3,name2)


Multiple_args()
Multiple_args('Dharani','Janani','Vishakan')

# Create a program to sum of three from the user input

num1 = int(input("Enter the Num 1\n"))
num2 = int(input("Enter the Num 2\n"))
num3 = int(input("Enter the Num 3\n"))

def Sum_of_three_number(n1,n2,n3):
    return n1 + n2 + n3

res = Sum_of_three_number(1,2,3)
print(res)
result = Sum_of_three_number(num1,num3,num2)
print(result)


def sum_of_two_number(a,b):
    return a+b

result_sum = sum_of_two_number(10,30)
print(result_sum)

def sum_of_num(**args):
    for i in args:
        print(i)
    print(args, sum(args))  # args is a list

sum_of_num(1,2)