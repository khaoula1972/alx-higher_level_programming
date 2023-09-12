#!/usr/bin/python3

"""
A module that contains a function that tells if the object is
"""


def is_same_class(obj, a_class):
    """
    A function that returns True if the object is exactly an instance
    of the specified class ; otherwise False.

    Args:
        obj (object): object being checked.
        a_class (class): class.

    Returns:
        True or False
    """
    return (type(obj) is a_class)
