#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Class that define a Rectangle

    Attributes:
        width (int): private width of rectangle
        height (int): private height of rectangle
        number_of_instances (int): number of instances class attribute
        print_symbol (any type): string symbol class attribute
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """attributes init method

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """return rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """return perimeter of rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """print str instance of rectangle class"""

        if self.__width == 0 or self.__height == 0:
            return ""
        string = []
        for n in range(self.height):
            symbol = str(self.print_symbol)
            string.append(symbol * self.width)
        return "\n".join(string)

    def __repr__(self):
        """return repr instance of rectangle class"""

        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """destroy instance"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """statis method that return the biggest rectangle

        Args:
            rect_1 (Rectangle): instance of class Rectangle
            rect_2 (Rectangle): instance of class Rectangle

        Raises:
            TypeError: rect_1 not instance of class Rectangle
            TypeError: rect_2 not instance of class Rectangle

        Returns:
            Rectangle: return the biggest rect
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
