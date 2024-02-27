#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_copy = matrix.copy()
    for i in matrix_copy:
        for j in i:
            j ** 2
    return matrix_copy
