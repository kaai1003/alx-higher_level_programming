#!/usr/bin/python3
def element_at(my_list, idx):
    """retrieve element list at index"""
    n = len(my_list)
    if idx < 0 or idx > n:
        return None
    else:
        return my_list[idx]
