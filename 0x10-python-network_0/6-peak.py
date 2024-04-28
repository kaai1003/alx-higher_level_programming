#!/usr/bin/python3
"""find the peak of the list of integers"""


def find_peak(list_of_integers):
    """find peak function
    Args
        list_of_integers: a list of integers
    """
    if list_of_integers == []:
        return None
    i = 0
    end = len(list_of_integers) - 1
    while i < len(list_of_integers):
        if i == 0:
            if list_of_integers[0] > list_of_integers[1]:
                return list_of_integers[0]
        elif i < end:
            if list_of_integers[i] > list_of_integers[i - 1] and list_of_integers[i] > list_of_integers[i + 1]:
                return list_of_integers[i]
        elif i == end:
            if list_of_integers[i] > list_of_integers[i - 1]:
                return list_of_integers[i]
        i += 1 
    return list_of_integers[i - 1]   
