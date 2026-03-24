#random number guessing game

import random
num = random.randint(1, 100)
while True:
    x = int(input("Enter your number: "))
    if num > x:
        print("Too low")
    elif num < x:
        print("Too high")
    else:
        print("Yes! Correct")
        break
