#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    y = (number * -1) % 10
    x = -y
else:
    x = number % 10
if (x > 5):
    print(f"Last digit of {number} is {x} and is greater than 5")
elif (x == 0):
    print(f"Last digit of {number} is {x} and is 0")
elif (x < 6):
    print(f"Last digit of {number} is {x} and is less than 6 and not 0")