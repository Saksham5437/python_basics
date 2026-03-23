def get_int():
    while True:
        try:
            x = int(input("What's X? "))
            return x
        except ValueError:
            pass
        
def main():
    x = get_int()
    print(f"x is {x}")

main()