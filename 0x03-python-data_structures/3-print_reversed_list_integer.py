#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """print list in reverse"""
    n = len(my_list) - 1
    while n >= 0:
        print("{}".format(my_list[n]))
        n -= 1
