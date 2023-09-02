#!/usr/bin/python3
"""

This module contains a function that adds two numbers

"""


def add_integer(a, b=98):
    """
    Function: add_integer

    Description: It takes two arguments and add them

    Args:
        a: the first number
        b: the second number

    Raises:
        TypeError: if a or b is not an integer or a float

    Returns:
        The sum of the two integers
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return (a + b)
