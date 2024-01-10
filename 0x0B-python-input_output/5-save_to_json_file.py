#!/usr/bin/python3
"""write object to file Module"""


import json


def save_to_json_file(my_obj, filename):
    """function that write an object to json file

    Args:
        my_obj (object): object to write
        filename (str): file name
    """
    with open(filename, mode="w") as jsonfile:
        json.dump(my_obj, jsonfile)
