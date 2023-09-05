#!/usr/bin/python3

"""

This module contains the solution to N Queen puzzle


"""

import sys


def init_board(n):
    """
    Function that initialize an empty board
    """
    return ([[0]*n for i in range(n)])


def is_safe(board, row, col, n):
    """
    Function that checks if it's safe to place a queen at the given row and col
    """
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def Nqueen(n):
    """
    Function that solves the puzzle and print possible solutions
    """
    solutions = []

    def backtrack(row):
        """
        Function that apply backstrack method to check if it's solvable
        """
        if row == n:
            solutions.append(list(board))
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1)

    board = [-1] * n
    backtrack(0)

    for solution in solutions:
        print([[i, solution[i]] for i in range(n)])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    Nqueen(n)
