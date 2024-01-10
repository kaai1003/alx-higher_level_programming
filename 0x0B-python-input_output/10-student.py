#!/usr/bin/python3
"""Student class Module"""


class Student:
    """Class Student
    """

    def __init__(self, first_name, last_name, age):
        """_summary_

        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return object dict

        Args:
            attrs (list): list of attributes
        """
        if attrs is None:
            return self.__dict__
        att_dict = {}
        for name, value in self.__dict__.items():
            if name in attrs:
                att_dict[name] = value
        return att_dict
