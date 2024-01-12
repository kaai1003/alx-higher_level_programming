#!/usr/bin/python3
"""Module Base Class"""


class Base:
    """Class Base

    Attributes:
        nb_objects (int) : private class attribute """
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor

        Args:
            id (int): base id
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
