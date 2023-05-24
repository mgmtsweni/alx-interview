#!/usr/bin/python3
""" Solution to the nqueens problem"""
import sys


def backtrack(r, n, cols, positive, negative, board):
    """ backtrack function to find solution"""
    if r == n:
        res = []
        for l in range(len(board)):
            res.extend([l, k] for k in range(len(board[l])) if board[l][k] == 1)
        print(res)
        return

    for c in range(n):
        if c in cols or (r + c) in positive or (r - c) in negative:
            continue

        cols.add(c)
        positive.add(r + c)
        negative.add(r - c)
        board[r][c] = 1

        backtrack(r+1, n, cols, positive, negative, board)

        cols.remove(c)
        positive.remove(r + c)
        negative.remove(r - c)
        board[r][c] = 0


def nqueens(n):
    """Solution to nqueens problem"""
    cols = set()
    positive_diag = set()
    negative_diag = set()
    board = [[0] * n for _ in range(n)]

    backtrack(0, n, cols, positive_diag, negative_diag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(n[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
