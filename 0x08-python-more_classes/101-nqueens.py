#!/usr/bin/python3
""" The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem.
"""
import sys


def position(board, row, col):
    """
    Find the right posision
    """
    for i in range(col):
        if board[i][1] == row or board[i][1] == row - (col - i) or \
                board[i][1] == row + (col - i):
            return False

    return True


def nqueens(board, col):
    """ Position the queens """
    if col >= N:
        print(board)
        return

    for i in range(N):
        if position(board, i, col):
            board[col] = [col, i]

            nqueens(board, col + 1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0, 0] for i in range(N)]

    nqueens(board, 0)
