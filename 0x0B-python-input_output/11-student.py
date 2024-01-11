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

    def reload_from_json(self, json):
        """reload attrs fron json file

        Args:
            json (dict): dictionary of attrs
        """
        for key in json:
            if key == "first_name":
                self.first_name = json[key]
            elif key == "last_name":
                self.last_name = json[key]
            elif key == "age":
                self.age = json[key]
