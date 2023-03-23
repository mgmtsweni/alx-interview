#!/usr/bin/python3
"""Change making module."""


def makeChange(coins, total):
    """Return: fewest number of coins needed to meet total"""
    if total <= 0:
        return 0
    count = 0
    index = 0
    sortedCoins = sorted(coins, reverse=True)
    i = len(coins)
    while total > 0:
        if index >= i:
            return -1
        if total - sortedCoins[index] >= 0:
            total -= sortedCoins[index]
            count += 1
        else:
            index += 1
    return count
