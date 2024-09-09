# take input and crate a class in python


class Person:

    def __init__(self):
        self.name = input("Enter the name \n")
        self.age = input("Enter your age\n")
        self.phone  = input("Enter your Mobile No:\n")

    def name_of_the_function_to_dispaly(self):
        print(f'Name is {self.name} ', f"Age is {self.age}", f"Phone is {self.phone}")



person1 = Person()

person1.name_of_the_function_to_display()
