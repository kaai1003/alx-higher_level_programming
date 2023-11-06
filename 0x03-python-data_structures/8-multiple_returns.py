#!/usr/bin/python3
def multiple_returns(sentence):
    """return tuple with length and first character of string"""
    if sentence == "":
        str_tuple = (0, None)
    else:
        str_tuple = (len(sentence), sentence[0])
    return str_tuple
