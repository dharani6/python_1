'''
### Task #4



- Write a Python program to calculate the area of a circle given its radius using the formula
``` area=π×r^2``` ( Take pie as 3.14)

'''
radius = float(input("enter the Radius value.!!!\n"))
area = 3.14*(radius**2)
print(f"area is equal = {area}")

area = lambda r: 3.14*(radius**2)

print(f"lambda function output {area(radius):.2f}")