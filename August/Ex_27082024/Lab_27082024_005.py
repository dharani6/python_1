# Function scope

def make_pizza(*toppings, base):
    print(toppings,base)

def make_pizza_2(base, *topping):
    print(topping,base)

 # this not allowed

make_pizza(("mushroom","tomoto",'cheese', base =="thin crust"))

make_pizza_2(base="dasa", "olive", "panner0") # Syntax ERROR postional arugumetn follows keyword argument

