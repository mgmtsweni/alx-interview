#!/usr/bin/python3
"""A Module to make change"""


def makeChange(coins, total):
    """Returns: fewest number of coins needed to meet total"""
    if total <= 0:
        return 0
    count = 0
    i = 0
    sorted_Coins = sorted(coins, reverse=True)
    l = len(coins)
    while total > 0:
        if i >= l:
            return -1
        if total - sorted_Coins[i] >= 0:
            total -= sorted_Coins[i]
            count+= 1
        else:
            i += 1
    return count
