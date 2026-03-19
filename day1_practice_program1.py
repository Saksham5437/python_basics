# program for calculating Simple Interest
#Taking the values from the user
P = float(input("Enter the principal amount : "))
R = float(input("Enter the rate of interest : "))
T = float(input("Enter the time in years : "))

# calculating the SI

SI = (P * T * R) / 100

#displaying the result

print(f"The Simple Interest is : {SI:,}")