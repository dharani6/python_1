#if loop if condition syntax

num = 8
if num == 5:
    print(str(num), "is not 5")
else:
    print(str(num),"Num is greter that 5",sep=" -- ")
num1 = int(input("Enter the Nummber 1"))
num2 = int(input("Enter the Nummber 2"))
num3 = int(input("Enter the Nummber 3"))
num4 = int(input("Enter the Nummber 4"))


if num1 > num2 and num1 > num3 and num1 > num4:
    print(f"num1--{num1} is greter of all the given number/n")
elif num2 > num1 and num2 > num3 and num2 > num4:
        print(f"num2--{num2} is greter of all the given number/n")
elif num3 > num1 and num3 > num2 and num3 > num4:
        print(f"num3--{num3} is greter of all the given number/n")
elif num4 > num1 and num4 > num2 and num4 > num3:
        print(f"number- {num4} is greter of all the given number/n")