
def outer_function():
    var1 = 30 # local int variable

    def inner_function():
        print(f"Innter_function1 {var1}")

    def inner_function2():
        print(f"innter function2 {var1}")
    print("outer function start or end")
    inner_function()
    inner_function2()


outer_function()