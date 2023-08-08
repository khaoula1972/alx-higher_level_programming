#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = int(str(number)[-1])
if number < 0:
    n = -n
print(f"Last digit of {number} is {n}", end = "")
if n < 6 and n != 0:
    print(" and is less than 6 and not 0")
elif n > 5:
    print(" and is greater than 5")
else:
    print(" and is 0")
