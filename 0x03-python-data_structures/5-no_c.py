#!/usr/bin/python3
def no_c(my_string):
    """remove c and C from string"""
    chars = list(my_string)
    i = 0
    while i < len(chars):
        if chars[i] == 'C' or chars[i] == 'c':
            chars.pop(i)
        else:
            i += 1
    new_string = "".join(chars)
    return new_string
