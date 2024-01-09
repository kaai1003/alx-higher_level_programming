#!/usr/bin/python3
"""write in file Module"""


def write_file(filename="", text=""):
    """write text to file using utf8

    Args:
        filename (str): name or path of file.
        text (str): text to write on the file.
    """
    with open(filename, "w", encoding="UTF-8") as r:
        r.write(text)
