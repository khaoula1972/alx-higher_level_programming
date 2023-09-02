#!/usr/bin/python3
def print_square(size):
    """
    Function: print_square

    Description: a function that prints a square with the character #.

    Args:
        size (int): the size of the squares sides

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is negative

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print('#' * size)
