'''### Task #8

✅ Triangle Classifier:


Write a program that classifies a triangle based on its side lengths.

Given three input values representing the lengths of the sides,

determine if the triangle is equilateral (all sides are equal),

isosceles (exactly two sides are equal), or scalene (no sides are equal).

Use an if-else statement to classify the triangle.
'''
Side1 =   float(input("Enter the length of a side1 of the Triangle\n"))
Side2 =   float(input("Enter the length of a side2 of the Triangle\n"))
Side3 =   float(input("Enter the length of a side3 of the Triangle\n"))

if Side1 != Side2 and Side2!=Side3 and Side3 != Side1:
    print(f"All the sides are not equal so Triangle is scalene")
elif Side1 == Side2 == Side3:
    print(f"All the sides are equal so given triable is equilateral")
elif Side1 == Side2 or Side3 == Side2 or Side3 ==Side1:
    print(f"2 sides of triangle is equal so the give Triangle is isosceles")