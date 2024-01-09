#!/usr/bin/python3
"""read file Module"""


def read_file(filename=""):
    """read file function

    Args:
        filename (str): name or path of file.
    """
    with open(filename, "r", encoding="utf-8") as r:
        print(r.read())
