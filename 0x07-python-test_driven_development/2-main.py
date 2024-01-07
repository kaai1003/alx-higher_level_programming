#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

#test1 matrix of lists with integers/floats
matrix = [
    [1, 2, 5],
    [1.4, 2.6, 8],
    [6, 7, 4]
]
print(matrix_divided(matrix, 2))
#test2 matrix of lists with different size
matrix = [
    [1, 2, 3, 6],
    [4, 5, 6]
]
try:
    print(matrix_divided(matrix, 3))
except Exception as e:
    print(e)
#test3 check divisor is not 0
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
try:
    print(matrix_divided(matrix, 0))
except Exception as e:
    print(e)
#test4 check divisor is integer/float
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
try:
    print(matrix_divided(matrix, "a"))
except Exception as e:
    print(e)
#test5 check lists elements is integer/float
matrix = [
    [1, 2, 3],
    [4, "b", 6]
]
try:
    print(matrix_divided(matrix, 3))
except Exception as e:
    print(e)
#test5 check matrix if is list of lists
matrix = [1, 2, 3]
try:
    print(matrix_divided(matrix, 3))
except Exception as e:
    print(e)