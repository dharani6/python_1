# Method overloading

# Python does not support method overloading

# in the traditional sense.


class Mathuthils(object):  # is -A object - Single inheritance

    # Method - overloading - Not support!
    def add(self, a,b):
        return a + b
    def add(self,a,b,c):
        return  a + b + c

    def add(self, a, b, c =10, d= 1):
        return a + b + c + d

math = Mathuthils()

op1 = math.add(1,2)
print(op1)
op2 = math.add(1,2,3)
print(op2)