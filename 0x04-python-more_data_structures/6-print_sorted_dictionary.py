#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """print sorted dict"""
    for k in sorted(a_dictionary.keys()):
        print("{}:".format(k), a_dictionary[k])