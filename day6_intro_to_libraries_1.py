#random choice
from random import choice

cards = choice(["heads", "tails"])
print(cards)

#randint
import random
num = random.randint(1,100)
print(num)

#random shuffle

import random
num = ["1", "2", "hi"]
number = random.shuffle(num)
for number in num:
    print(number)