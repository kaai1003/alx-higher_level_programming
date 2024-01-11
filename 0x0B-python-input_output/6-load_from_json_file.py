#!/usr/bin/python3
"""get object from file Module"""


import json


def load_from_json_file(filename):
    """function that get an object from json file

    Args:
        filename (str): file name
    """
    with open(filename, mode="r") as jsonfile:
        return json.load(jsonfile)
