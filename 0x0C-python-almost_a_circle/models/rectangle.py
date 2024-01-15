#!/usr/bin/python3
"""Rectangle Class module"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle constructor

        Args:
            width (int): width of rectangle
            height (int): heigth of rectangle
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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate area of rectangle"""
        return self.width * self.height

    def display(self):
        """print rectangle with "#" """
        for y in range(self.y):
            print("")
        for i in range(self.height):
            print(" " * self.x, end="")
            for j in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """print rectangle representation"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """update attributes
        Args:
            args (list): list of arguments
        """
        if args:
            self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) == 5:
                self.y = args[4]
        elif kwargs:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "width":
                    self.width = kwargs[key]
                elif key == "height":
                    self.height = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                elif key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        """return dict of rectangle"""
        return {'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width}
