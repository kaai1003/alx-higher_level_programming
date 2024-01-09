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
    """Class Rectangle"""