#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    new = list()
    L = len(matrix)
    if L == 0:
        return None
    for i in range(L):
        C = len(matrix[i])
        for j in range(C):
            new[i][j] = matrix[i][j]
    return (new)