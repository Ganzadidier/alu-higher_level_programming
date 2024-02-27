#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_copy = []
    for i in matrix:
	    matrix_copy.append(i)
	    for j in range(len(i)):
	        i[j] = i[j]**2
    return matrix_copy
