#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """calculate square of matrix elements"""
    square = [[(row[i]**2)for i in range(len(matrix))] for row in matrix]
    return square
