#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """replace element in list"""
    n = len(my_list)
    if idx < 0 or idx >= n:
        return my_list
    else:
        my_list[idx] = element
        return my_list
