#!/usr/bin/python3
"""
This module conatins a class
"""


class MyInt(int):
    """
    This is int class child, but not really a good child
    He's a REBEL!
    """
    def __eq__(self, other):
        """ He inverted equality """
        return super().__ne__(other)

    def __ne__(self, other):
        """ And made negativity an equality """
        return super().__eq__(other)

    """ Dont be like MyInt """
