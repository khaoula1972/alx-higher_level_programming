#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    C = len(matrix[0])
    L = len(matrix)
    for i in range(L):
        for j in range(C):
            e = " "
            if j == C - 1:
                e = "\n"
            print("{:d}".format(matrix[i][j]), end=e)
