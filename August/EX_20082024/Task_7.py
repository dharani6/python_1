'''
### Task #7

✅ Leap Year Checker:

Create a program that determines whether a given year is a leap year.

A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.

Use an if-else statement to make this determination.
'''

year = int(input("Entre the year to find out its leap year or not !!!\n"))

if year%4 ==0 or year%400:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")