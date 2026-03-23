#program to show exception handling by using zero division error and ValueError 

def main():
       while True:
            try:
                x = int(input("Enter X: "))
                y = int(input("Enter Y: "))
                print(x/y)
            except ZeroDivisionError:
                print("Cannot divide by zero!")
            except ValueError:
                print("Please enter a valid number!")
            else:
                 break
            

main()



    
    
    