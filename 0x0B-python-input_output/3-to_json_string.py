#!/usr/bin/python3
"""JSON repr Module"""


import json


def from_json_string(my_str):
    """return json representation

    Args:
        my_str (str): string variable
    """

    return json.dumps(my_str)
