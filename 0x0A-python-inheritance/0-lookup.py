#!/usr/bin/python3
"""module return attributes and methods of object"""


def lookup(obj):
    """function that return list of attributes and methods of object
    Args:
        obj (object): variable to abject
    """
    return dir(obj)
