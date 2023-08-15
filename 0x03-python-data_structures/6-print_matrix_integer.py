#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    L = len(matrix)
    for i in range(L):
        C = len(matrix[i])
        for j in range(C):
            e = " "
            if j == C - 1:
                e = "\n"
            print("{:d}".format(matrix[i][j]), end=e)
