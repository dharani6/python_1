"""
Method Overriding - Same name in the parent and child class

child always override the parent functions

super means call my parent function

"""

class GrandFather:

    x = 10

    def home(self):
        print("Old Home")

class Father(GrandFather):

    a = 10

    def home(self):
        print("1BHK")
        print(self.a)
        print(super().x)

class Son(Father):

    b = 10

    def home(self):
        super().home()  # Father Behaviour by super()
        print(super().a) # Father Atributes by super()
        print("No House")
        print(self.b)


        # Self - me
        # super() -- Parent, super class, father


dharnai = Son()
dharnai.home()
print(dharnai.x)