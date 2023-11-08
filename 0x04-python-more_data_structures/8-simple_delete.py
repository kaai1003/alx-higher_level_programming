#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for k in a_dictionary.keys():
        if k == key:
            a_dictionary.pop(k)
    return a_dictionary
