#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """calculate square of matrix elements"""
    square = [[(n**2)for n in rows] for rows in matrix]
    return square
