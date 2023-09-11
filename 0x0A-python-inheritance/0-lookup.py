#!/usr/bin/python3

"""

This module contains a function that returns attributes and methods

"""


def lookup(obj):
    """
    lookup: a function that returns the list of available attributes
    and methods of an object:

    Arg:
        obj: the object
    
    """
    return (dir(obj))
