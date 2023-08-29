#!/usr/bin/python3
"""
A class: Square

A square is a four-sided polygon with all side of equal
length and all angles right angles.
"""


class Square:
    """
    This is Square class
    """

    def __init__(self, size):
        """
        Initialize a square with the given side length.

        Args:
            size: The length of all sides of the square.
            type: float or int
        """
        self.__size = size
