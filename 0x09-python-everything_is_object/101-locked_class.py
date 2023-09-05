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

    def __setattr__(self, attr, value):
        """
        Method that allows the creation of first_name attribute but prevents
        the creation of any other instance attributes.
        """
        msg = "'LockedClass' object has no attribute"
        if attr == 'first_name':
            super().__setattr__(attr, value)
        else:
            raise AttributeError(msg+" '{}'".format(attr))
