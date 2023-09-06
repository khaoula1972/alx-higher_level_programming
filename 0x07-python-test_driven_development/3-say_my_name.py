#!/usr/bin/python3


"""

This module prints my name

"""


def say_my_name(first_name, last_name=""):
    """
    Function: say_my_name

    Description: a function that prints My name is <first name> <last name>

    Args:
        first_name: the name
        last_name: family name

    Raises:
        TypeError: if the arguments passed aren't strings

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
