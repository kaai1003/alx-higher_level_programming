#!/usr/bin/python3
"""find the peak of the list of integers"""


def find_peak(list_of_integers):
    """find peak function
    Args
        list_of_integers: a list of integers
    """
    if list_of_integers == []:
        return None
    length = len(list_of_integers)
    start = 0
    end = len(list_of_integers) - 1

    if list_of_integers[start] > list_of_integers[start + 1] and\
            start < end:
        return list_of_integers[start]
    elif list_of_integers[end] > list_of_integers[end - 1] and\
            end > start:
        return list_of_integers[end]
    while start <= end:
        mid = (start + end) // 2
        if (mid == 0 or
            list_of_integers[mid] >= list_of_integers[mid - 1]) and\
            (mid == length - 1 or
                list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid - 1]:
            end = mid - 1
        else:
            start = mid + 1
    return None
