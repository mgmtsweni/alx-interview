#!/usr/bin/python3

def isWinner(x, nums):
    """Returns the name of the winner"""
    if not nums or x < 1 or x > 10000:
        return None

    b = sum(num == 1 or num % 2 == 0 for num in nums)
    m = len(nums) - b

    if b > m:
        return "Ben"
    elif b < m:
        return "Maria"
    else:
        return None
