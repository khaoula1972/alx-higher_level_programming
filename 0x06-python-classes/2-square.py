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

    def __init__(self, size=0):
        """
        Initialize a square with the given side length.

        Args:
            size: The length of all sides of the square.
            type: positive integer
        """
        if not isinstance(size, (int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
