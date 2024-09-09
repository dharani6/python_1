# Method overriding.
# Says that, Child or subclass can have same method name as the parent or super class

class Shape:

    def area(self):
        print("Print the AREA of the shape")

class Rectangle(Shape): # Is-A -- Single Inheritance

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * 3.14


shape1 = Rectangle(3,4)
print(shape1.area())

shape2 = Circle(8)
print(shape2.area())