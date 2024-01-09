#!/usr/bin/python3
"""print text Module"""


def text_indentation(text):
    """split text and print each part

    Args:
        text (str): text to be splited and printed

    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    p = ""
    for c in text:
        if c == "." or c == "?" or c == ":":
            p += c
            print(p)
            print("")
            p = ""
            continue
        if c == " " and p == "":
            continue
        p += c
    if c == " ":
        p = p[:-1]
    print(p, end='')
