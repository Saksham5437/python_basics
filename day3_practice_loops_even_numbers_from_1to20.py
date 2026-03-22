#Program to print even numbers from 1 to 20

i = 1
print("The even numbers from 1 to 20 are : ")

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

    i += 2

