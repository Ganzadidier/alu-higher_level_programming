#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
     squared_matrix = [list(map((lambda x: x * x), i)) for i in matrix]

     return squared_matrix
