#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """print list in reverse"""
    my_list.reverse()
    for n in my_list:
        print("{:d}".format(n))
