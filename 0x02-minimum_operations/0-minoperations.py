#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """ calculates the fewest number of operations needed 
        to result in exactly n H characters in the file.
        Returns an integer
    """
    if not isinstance(n, int):
        return 0

    op = 0
    minOp = 2
    while n > 1:
        while n % minOp == 0:
            op += minOp
            n /= minOp
        minOp += 1
    return op
