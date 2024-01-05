#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Class that define a Rectangle

    Attributes:
        width (int): private width of rectangle
        height (int): private height of rectangle
    """
    def __init__(self, width=0, height=0):
        """attributes init method

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width of rectangle

        Args:
            value (int): value of width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """get rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height of rectangle

        Args:
            value (int): value of height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
