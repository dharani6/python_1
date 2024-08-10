with open("output.txt", "w+") as file:
    print("Hello", "World", sep="-", end="!", file=file, flush=True)
    print(50, 1000, 3.142, "Hello World", file=file, flush=True)
