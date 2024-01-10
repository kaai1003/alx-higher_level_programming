#!/usr/bin/python3
"""class object json Module"""


def class_to_json(obj):
    """return json representation
    of class object

    Args:
        obj (object): class object
    """

    return obj.__dict__
