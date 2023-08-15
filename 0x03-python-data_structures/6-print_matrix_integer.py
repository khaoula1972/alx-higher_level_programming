#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    L = len(matrix)
    if L == 0:
        print("{}".format("[[]]"))
    for i in range(L):
        C = len(matrix[i])
        for j in range(C):
            if j < C - 1:
                e = " "
            elif j == C - 1:
                e = ""
            print("{:d}".format(matrix[i][j]), end=e)
