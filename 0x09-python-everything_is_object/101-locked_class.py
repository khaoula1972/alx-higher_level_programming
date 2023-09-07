#!/usr/bin/python3

"""
This module contains a class with no class or object attribute
that prevents the user from dynamically creating new instance attributes
except if the new instance attribute is called first_name.
"""


class LockedClass:
    """
    Secret class
    """

    __slots__ = ['first_name']
