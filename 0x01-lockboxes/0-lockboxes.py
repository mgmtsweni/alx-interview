#!/usr/bin/python3

def canUnlockAll(boxes):
    visited = [False] * len(boxes)
    stack = [0]
    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            stack.extend(boxes[current])
    return all(visited)
