#program to find whether the given number is even or odd

#defining the main function
def main():
    x = int(input("Enter the number : "))
    if is_even(x):
        print("The number is even. ")
    else:
        print("The number is odd.")

#defining the function to check whether the number is even or odd
def is_even(n):
    return n % 2 == 0
    
#defining the main function    
main()