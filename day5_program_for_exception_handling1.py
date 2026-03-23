#Example program to show exception handling

try:
    x = int(input("Enter a number: "))
    print(x)
except ValueError:
    print("Please enter a valid number!")
    

