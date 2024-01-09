#!/usr/bin/python3
"""BaseGeometry Module"""


class BaseGeometry:
    """basegeometry class"""

    def area(self):
        """area Method

        Raises:
            Exception: area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Value validation Method

        Args:
            name (string): string variable
            value (int): value
        """
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle Class inherate from BaseGeometry

    Attributes:
        width (int): private attribute width
        heigth (int): private attribute heigth
    """

    def __init__(self, width, heigth):
        """init magic method

        Args:
            width (int): width of rectangle
            heigth (int): heigth of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("heigth", heigth)
        self.__heigth = heigth

    def area(self):
        """Rectangle area calculation
        return rectangle area
        """
        return self.__width * self.__heigth

    def __str__(self):
        """print rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__heigth)


class Square(Rectangle):
    """Class Square inherate from Rectangle class"""

    def __init__(self, size):
        """init size attribute

        Args:
            size (int): size square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculate square area"""
        return self.__size ** 2

    def __str__(self):
        """print rectangle description"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
