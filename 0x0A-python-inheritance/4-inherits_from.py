#!/usr/bin/python3
"""Module check inherited class"""


def inherits_from(obj, a_class):
    """check object inherited class

    Args:
        obj (object): object to check
        a_class (class): class
    """
    if issubclass(type(obj), a_class):
        if not type(obj) is a_class:
            return True
    return False
