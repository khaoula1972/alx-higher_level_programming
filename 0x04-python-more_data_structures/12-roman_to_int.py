#!/usr/bin/python3
def roman_to_int(roman_string):

    # To check, if the given variable is string or not
    if not (isinstance(roman_string, str)):
        return (0)

    numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    number = 0

    for i, x in enumerate(roman_string):
        if (i + 1 < len(roman_string) and
                numbers[x] < numbers[roman_string[i + 1]]):
            number -= numbers[x]
        else:
            number += numbers[x]

    return (number)
