#!/usr/bin/python3
"""Square Class module"""
from models.rectangle import Rectangle
import json
import os
import sys


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """Square constructor

        Args:
            size (int): size of square
            x (int): x cord
            y (int): y cord
            id (int): id of square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get size square"""
        return self.width

    @size.setter
    def size(self, value):
        """set square size
        Args:
            value (int): square size
        """
        self.width = value
        self.height = value

    def __str__(self):
        """print square representation"""

        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """update attributes
        Args:
            args (list): list of arguments
        """
        if args:
            self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "size":
                    self.size = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                elif key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        """return dict of Square"""
        return {'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y}
