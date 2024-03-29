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

    def to_json(self):
        """return object dict"""
        return self.__dict__
