#!/usr/bin/python3

"""
This module contains a function that multiplies two matrices
"""


def matrix_mul(m_a, m_b):
    """
    Function: matrix_mul

    Description: a function that multiplies 2 matrices

    Args:
        m_a: the first matrice
        m_b: the second matrice

    Raises:
        TypeError: matrices of list of lists of floats or integer
        ValueError: case of Empty matrices, or if the matrices can't be
            multiplied.

    """
    if not (isinstance(m_a, list)):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for element in row:
            if not (isinstance(element, int) or isinstance(element, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not (isinstance(element, int) or isinstance(element, float)):
                raise TypeError("m_b should contain only integers or floats")

    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Now let's move to the multiplication:
    C = []
    for i in range(len(m_a)):
        D = []
        for j in range(len(m_b[0])):
            S = 0
            for k in range(len(m_b)):
                S += m_a[i][k] * m_b[k][j]
            D.append(S)
        C.append(D)

    return (C)
