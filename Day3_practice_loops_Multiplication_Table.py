#Program to display Multiplication table of a number entered by the user 

n = int(input("Enter the number: "))

i = 0

while i <= 10:
    print(f"{n} x {i} = {n*i}")
    i += 1