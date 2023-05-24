#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """
        calculates the fewest number of operations needed
        to result in exactly n H characters in the file.
    """
    if not isinstance(n, int):
        return 0

    opp = 0
    min_opp = 2
    while n > 1:
        while n % min_opp == 0:
            opp += min_opp
            n /= min_opp
        min_opp += 1
    return opp
