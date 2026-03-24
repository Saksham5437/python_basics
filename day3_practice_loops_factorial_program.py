#program to give factorial of a given number by the user

def main():
    x = int(input("Enter the factorial number: "))
    ans = 1
    for i in range(1, x+1):
        ans = ans * i
    print(f"The factorial of {x} is {ans}")

main()