#!/usr/bin/python3
"""
A module that contains a function that tells if the object is
from a specified class
"""


def is_kind_of_class(obj, a_class):
    """
    A function that returns True if the object is kind of an instance
    of the specified class ; otherwise False.
    Args:
        obj (object): object being checked.
        a_class (class): class.
    Returns:
        True or False
    """

    return (isinstance(obj, a_class))
