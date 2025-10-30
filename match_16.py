x = int(input("Enter a number between 1 and 3: "))

match x:
    case 1:
        print("Value of x is one")
    case 2:
        print("Value of x is two")
    case 3:
        print("Value of x is three")
    case _:
        print("Invalid")
