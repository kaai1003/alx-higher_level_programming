#!/usr/bin/python3
"""Module check kind of class"""


def is_kind_of_class(obj, a_class):
    """check object kind class

    Args:
        obj (object): object to check
        a_class (class): class
    """
    if isinstance(obj, a_class):
        return True
    return False
