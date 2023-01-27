#!/usr/bin/python3
"""
Create a function that returns Pascal's triangle
"""


def pascal_triangle(n: int):
    """
        Returns a a list of lits reprisenting
        Pascal's triangle of a given integer.
    """
    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        level = [1]
        for j in range(1, i + 1):
            level.append(level[j - 1] * (i - j + 1) // j)
        triangle .append(level)
    return triangle
