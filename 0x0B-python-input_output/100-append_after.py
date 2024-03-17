#!/usr/bin/python3
"""append line to file Module"""


def append_after(filename="", search_string="", new_string=""):
    """_summary_

    Args:
        filename (str): name of the file.
        search_string (str): line string reference.
        new_string (str): new line to append.
    """
    with open(filename, mode="+a") as f:
        lines = f.readlines()
        for line in lines:
            if line.find(search_string) == -1:
                continue
            
