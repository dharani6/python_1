'''
OOPs
Class - BluePrint
Object - Instance of Class
Encapsulation - Private __, protected __, public
Inheritance - Single, multiple, multilevel, heri, hybrid
ply - method overiding, method overloading(x)
seld, super, __init__

abstraction
Hide the details and show what is required.
car - with key _  __private, type --> public,

car -> multipe - engine, gearbox
car -> drive -> engine, gearbox ??


'''

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self,name):
        self.name = name

    @abstactmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("bark")

dog = Dog("PP")
dog.sound()


