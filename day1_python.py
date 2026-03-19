#program to input name and print the same
name=input("Enter your name : ")
print("Hello, ", end="")
print(f"{name}")

#entering the age
age=int(input("Enter your age : "))
print("Your age is : ", age)

#age after 5 years
print("Your age after 5 years will be : ", age+5)

#small general calculator
a=int(input("Enter the first digit : "))
b=int(input("Enter the second digit : "))
print("The sum is : ", round(a+b, 2))
print("The difference is : ", round(a-b, 2))
print("The product is : ", round(a*b, 2))
print("The quotient is : ", round(a/b, 2))
print("The remainder is : ", round(a%b, 2))