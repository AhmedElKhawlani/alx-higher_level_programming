#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print('$')
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[0]) - 1):
                print("{:d} ".format(matrix[i][j]), end='')
            print("{:d}".format(matrix[i][j + 1]), end='')
            print('$')
