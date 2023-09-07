#!/usr/bin/python3

"""

This module contains a function that multiplies two matrices

"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function: lazy_matrix_mul

    Description: a function that multiplies 2 matrices

    Args:
        m_a: the first matrice
        m_b: the second matrice

    Raises:
        TypeError: matrices of list of lists of floats or integer
        ValueError: case of Empty matrices, or if the matrices can't be
            multiplied.

    """
    return (np.matmul(m_a, m_b))
