#!/usr/bin/python3
def print_last_digit(number):
    n = int(str(number)[-1])
    print("{:d}".format(n), end="")
    return (n)
