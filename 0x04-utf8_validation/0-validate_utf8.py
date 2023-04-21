#!/usr/bin/python3
"""utf8 validation problem"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    def countbit(num):
        count = 0
        for i in range(7, -1, -1):
            if num & (1 << i):
                count += 1
            else:
                break
        return count
    count = 0
    for d in data:
        if not count:
            count = countbit(d)
            if count == 0:
                continue
            if count == 1 or count > 4:
                count -= 1
                return False
            else:
                count -= 1
                if countbit(d) != 1:
                    return False
    return count == 0
