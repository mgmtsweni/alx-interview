#!/usr/bin/python3
""" Rotate 90 Degrees Clockwise"""
import itertools


def rotate_2d_matrix(matrix):
    """rotate a matrix 90 degrees clockwise"""

    n = len(matrix[0])

    """ for i in range(n - 1, -1, -1):
        for j in range(0, n):"""
    for i, j in itertools.product(range(n - 1, -1, -1), range(n)):
        matrix[j].append(matrix[i].pop(0))
