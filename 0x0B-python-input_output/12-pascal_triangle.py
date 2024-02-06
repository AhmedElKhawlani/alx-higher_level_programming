#!/usr/bin/python3
"""
Module that defines a function that returns a list of lists of
integers representing the Pascal’s triangle.
"""


def pascal_triangle(n):
    if n <= 0:
        return []
    P = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i:
                P[i][j] = 1
            else:
                P[i][j] = P[i - 1][j] + P[i - 1][j - 1]
    for L in P:
        while 0 in L:
            L.remove(0)
    return P
