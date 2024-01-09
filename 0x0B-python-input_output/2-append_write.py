#!/usr/bin/python3
"""append text Module"""


def append_write(filename="", text=""):
    """append text to file

    Args:
        filename (str): name or path of file.
        text (str): text to append.
    """

    with open(filename, mode="a", encoding="utf-8") as r:
        return r.write(text)
