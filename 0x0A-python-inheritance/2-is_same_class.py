#!/usr/bin/python3
"""Module check instance of object"""


def is_same_class(obj, a_class):
    """check object instance class

    Args:
        obj (object): object to check
        a_class (class): class
    """
    if type(obj) is a_class:
        return True
    return False
