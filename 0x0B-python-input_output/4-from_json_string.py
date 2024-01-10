#!/usr/bin/python3
"""covert fron JSON string Module"""


import json


def from_json_string(my_str):
    """function that convert json string to python object

    Args:
        my_str (str): json string
    """
    return json.loads(my_str)
