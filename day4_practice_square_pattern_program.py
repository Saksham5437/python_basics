#Pattern program to print a square of stars

n = int(input("Enter the number: "))

def square(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()

def main():
    square(n)

main()            