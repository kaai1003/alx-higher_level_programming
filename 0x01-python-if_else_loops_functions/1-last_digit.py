#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldigit = abs(number) % 10
if number < 0:
    ldigit = -ldigit
if ldigit > 5:
    print(f"Last digit of {number} is {ldigit} and is greater than 5")
elif ldigit == 0:
    print(f"Last digit of {number} is {ldigit} and is 0")
elif ldigit < 6:
    print(f"Last digit of {number} is {ldigit} and is less than 6 and not 0")
