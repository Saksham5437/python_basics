#program to show exception handling by using zero division error 

def main():
        try:
            x = int(input("Enter X: "))
            y = int(input("Enter Y: "))
            return x/y
        except ZeroDivisionError:
            print("Cannot divide by zero!")

main()



    
    
    