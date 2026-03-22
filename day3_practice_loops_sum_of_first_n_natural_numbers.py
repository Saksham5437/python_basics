#Program to find the sum of first n natural numbers

n = int(input("Enter the number: "))

i = 1
for i in range(n):
    sum = (n*(n+1))/2
    i += 1

print("The sum of first", n, "natural numbers is: ", sum)    
