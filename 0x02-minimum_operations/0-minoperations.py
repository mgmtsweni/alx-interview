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
    while (minOp <= n):
        if not (n % minOp):
            n = int(n / minOp)
            op += minOp
            minOp = 1
        minOp += 1
    return op
