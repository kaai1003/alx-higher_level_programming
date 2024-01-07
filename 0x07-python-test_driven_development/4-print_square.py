#!/usr/bin/python3
"""print square module"""


def print_square(size):
    """print square using "#"

    Args:
        size (int): size of square
    """
    if not isinstance(size, int):
            raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for r in range(size):
        print("#" * size)
