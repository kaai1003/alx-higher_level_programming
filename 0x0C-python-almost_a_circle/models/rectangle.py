#!/usr/bin/python3
"""Rectangle Class module"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle constructor

        Args:
            width (int): width or rectangle
            height (int): heigth or rectangle
            x (int): x cord
            y (int): y cord
            id (int): id of rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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
        self.__height = value

    @property
    def x(self):
        """get x cord"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x cord

        Args:
            value (int): value of x
        """
        self.__x = value

    @property
    def y(self):
        """get y cord"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y cord

        Args:
            value (int): value y
        """
        self.__y = value
