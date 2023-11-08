#!/usr/bin/python3
def uniq_add(my_list=[]):
    """return sum of unique elments in list"""
    unique = set(my_list)
    sum = 0
    for n in unique:
        sum = sum + n
    return sum
