#!/usr/bin/python3
"""pascal triangle Module"""


def pascal_triangle(n):
    """_summary_

    Args:
        n (int): pascal traingle n
    """
    pt_list = []
    if n <= 0:
        return pt_list
    for i in range(n):
        if i == 0:
            pt_list.append([1])
        elif i == 1:
            pt_list.append([1, 1])
        else:
            sub_list = []
            for j in range(i + 1):
                if j == 0:
                    sub_list.append(1)
                elif j == i:
                    sub_list.append(1)
                else:
                    sub_list.append(pt_list[i - 1][j - 1] + pt_list[i - 1][j])
            pt_list.append(sub_list)
    return pt_list
