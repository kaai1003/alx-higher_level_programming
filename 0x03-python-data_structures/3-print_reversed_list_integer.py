#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """print list in reverse"""
    if my_list:
        for n in my_list[::-1]:
            print("{:d}".format(n))