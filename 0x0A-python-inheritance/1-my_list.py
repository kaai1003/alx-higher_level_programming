#!/usr/bin/python3
"""module class MyList"""


class MyList(list):
    """Class MyList inherits from list
    """

    def print_sorted(self):
        """print sorted list"""
        sorted_list = sorted(list(self))
        print(sorted_list)
