# Triangle Clasifier
# side1 == side2 == side 3 ->  Eq.
# side 1 == side 2 or side 2 == side 3 or side 1 == side 3 -> ISO
# else -> Scalene
try:
    side1 = int(input("Enter the triable side 1\n"))
    side2 = int(input("Enter the triable side 2\n"))
    side3 = int(input("Enter the triable side 3\n"))



    def Triangle_Type(side1, side2, side3):
        if side1 == side2 == side3:
            print("Trianble is equlator")
        elif side1 == side2 or side2 == side3 or side1 == side3:
            print("triable is isolatral")
        else:
            print("Scalene")
except Exception as ee:
    print (ee)
Triangle_Type(side1, side2, side3)
