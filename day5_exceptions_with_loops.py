while True:
    try:
        x = int(input("What's X? "))
    except ValueError:
        print("X is not an integer.")
    else:
        break
print(f"x is {x}")