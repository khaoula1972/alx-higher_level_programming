#!/usr/bin/python3
"""
This module contains a class to improve geometry
"""


class BaseGeometry:
    """
    This is a class o geometry
    """
    def area(self):
        """
        This method raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method validates value
        """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
