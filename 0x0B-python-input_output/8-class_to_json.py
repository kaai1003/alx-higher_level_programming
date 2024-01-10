#!/usr/bin/python3
"""class object json Module"""


import json


def class_to_json(obj):
    """return json representation
    of class object

    Args:
        obj (object): class object
    """

    return json.dumps(obj.__dict__)
