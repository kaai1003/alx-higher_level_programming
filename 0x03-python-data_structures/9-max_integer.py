#!/usr/bin/python3
def max_integer(my_list=[]):
    """return the biggest integer in list"""
    if not my_list:
        return None
    else:
        big_int = my_list[0]
        for n in my_list:
            if n > big_int:
                big_int = n
    return big_int
