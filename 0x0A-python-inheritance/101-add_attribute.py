#!/usr/bin/python3
"""
This module contains a function that add attributes if possible
"""


def add_attribute(obj, attr_name, attr_value):
    """
    can add a new attribute to an object
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
