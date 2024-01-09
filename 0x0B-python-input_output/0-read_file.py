#!/usr/bin/python3
"""read file Module"""


def read_file(filename=""):
    """read file function

    Args:
        filename (str): name or path of file.
    """
    with open(filename, encoding="UTF8") as r:
        str = r.read()
        if str != "":
            print(str)