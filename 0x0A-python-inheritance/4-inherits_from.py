#!/usr/bin/python3
"""
Module that checks inherence
"""


def inherits_from(obj, a_class):
    """
    Function that returns False or True if there's an inherence
    """
    return not type(obj) is a_class and issubclass(type(obj), a_class)
