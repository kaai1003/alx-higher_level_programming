#!/usr/bin/python3
"""addition of 2 numbers module"""


def add_integer(a, b=98):
    """function do the addition of two numbers
        and return the result a + b
    Args:
        a: first number
        b: second number
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(a) == float:
        a = int(a)
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    elif type(b) == float:
        b = int(b)
    return int(a + b)
