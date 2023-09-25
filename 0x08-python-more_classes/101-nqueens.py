#!/usr/bin/python3
"""Solves the N-queens puzzle and prints all solutions."""

import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at (row, col)."""

    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N):
    """Solve the N-queens puzzle and print solutions."""

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def recursive_solve(row):
        if row == N:
            solutions.append([[i, board[i].index(1)] for i in range(N)])
            return

        for col in range(N):
            if is_safe(board, row, col):
                board[row][col] = 1
                recursive_solve(row + 1)
                board[row][col] = 0

    recursive_solve(0)

    for solution in solutions:
        print(solution)
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
