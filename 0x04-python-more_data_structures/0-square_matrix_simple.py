#!/usr/bin/python
def square_matrix_simple(matrix=[]):
    new = list()
    L = len(matrix)
    C = len(matrix[0])
    if L == 0:
        return None
    for i in range(L):
        k = list()
        for j in range(C):
            k.append(matrix[i][j]**2)
        new.append(k)
    return (new)
