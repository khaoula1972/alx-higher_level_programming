#!/usr/bin/python3

"""

This module contains a class that inherits from list

"""


class MyList(list):
    """

    This is a class MyList that inherits from list

    """
    def __init__(self):
        """
        Initialization..
        """
        super().__init__()

    def print_sorted(self):
        """
        Public instance method that prints the list, but sorted
        """
        print(sorted(self))
