# Match case statement in Python

name = input("What's your name : ")

match name:
    case "Saksham" | "Rishi" | "Ningu":
        print("Studies is BMSIT")
    case "Laghu":
        print("Studies in RV")
    case _:
        print("Unknown name")