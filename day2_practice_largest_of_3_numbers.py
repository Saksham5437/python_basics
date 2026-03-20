#Program to find out the largest of threee numbers

#taking the input of three numbers
n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the second number : "))
n3 = int(input("Enter the third number : "))

#finding the largerst number

if n1 > n2 and n2 > n3:
    print("The largest number is :", n1)
elif n2 > n1 and n1 > n3:
    print("The largest number is : ", n2)
else:
    print("The largest number is :", n3)

    