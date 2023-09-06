#!/usr/bin/python3


"""

This module takes a matrix and div then divide them

"""


def matrix_divided(matrix, div):
    """
    Function: matrix_divided

    Description: a function that divides all elements of a matrix.

    Args:
        matrix: the matrix we're gonna use to divide
        div: the divisor

    Returns:
        The new divided matrix

    """
    # The messages
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    msg_size = "Each row of the matrix must have the same size"
    msg_div_type = "div must be a number"
    msg_div_zero = "division by zero"

    if not isinstance(matrix, list):
        raise TypeError(msg_type)
    else:
        if matrix == []:
            raise TypeError(msg_type)
        for element in matrix:
            if not isinstance(element, list):
                raise TypeError(msg_type)
            else:
                length = len(matrix[0])
                if len(element) != length:
                    raise TypeError(msg_size)
                for elt in element:
                    if not (isinstance(elt, int) or isinstance(elt, float)):
                        raise TypeError(msg_type)

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError(msg_div_type)
    elif div == 0:
        raise ZeroDivisionError(msg_div_zero)

    new = []

    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new.append(new_row)

    return (new)
