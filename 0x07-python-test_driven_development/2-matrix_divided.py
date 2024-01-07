#!/usr/bin/python3
"""matrix division module"""
def matrix_divided(matrix, div):
    """a function that devid each member of matrix 
        return the new matrix
    Args:
        matrix: matrix list of lists
        div: divisor integer of float
    """
    if (div == 0 ):
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    check_matrix(matrix)
    new_matrix = []
    for sublist in matrix:
        new_list = []
        for n in sublist:
            new_list.append(round(n / div, 2))
        new_matrix.append(new_list)
    return (new_matrix)

def check_matrix(matrix):
    """function to check matrix 
        matrix should be list of list,
        element of lists should be integers/floats,
        size of lists should be the same
    Args:
        matrix: 
    """
    if not (all(isinstance(item, list) for item in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for sublist in matrix:
        if not (all(isinstance(n, (int, float)) for n in sublist)):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    lists_length = set(len(list) for list in matrix)
    if len(lists_length) != 1:
        raise TypeError("Each row of the matrix must have the same size")