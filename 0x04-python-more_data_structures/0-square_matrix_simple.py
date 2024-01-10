#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    M = [[0] * len(matrix[0]) for i in range(len(matrix))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            M[i][j] = matrix[i][j] ** 2
    return M
