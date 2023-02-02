#!/usr/bin/python3
"""Lockbox Challange"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened or not
        Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    """
    if ((type(boxes) is not list) or len(boxes) == 0):
        return False

    visited = [False] * len(boxes)
    stack = [0]

    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            stack.extend(boxes[current])

    return all(visited)
