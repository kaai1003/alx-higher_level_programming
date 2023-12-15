#!/usr/bin/python3
"""Class that Define a Square"""


class Square:
    """Class Square

    Attributes:
        size(int): size of square
        position(int): print position
    """
    def __init__(self, size=0, position=(0, 0)):
        """Method initialisation
        
        Args:
            size(int): size of square
            position(int): print position
        """
        self.size = size
        self.position = position
    @property
    def size(self):
        """getter Property of size"""
        return self.__size
    @size.setter
    def size(self, value):
        """Setter Proprety of size
        
        Args:
            value(int): size value
        """
        if not isinstance(value, int):
            raise Exception("size must be an integer")
        elif value < 0:
            raise Exception("size must be >= 0")
        else:
            self.__size = value
    @property
    def position(self):
        """getter Property of position"""
        return self.__position
    @position.setter
    def position(self, value):
        """Setter Proprety of position
        
        Args:
            value(int): position value
        """
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    def area(self):
        """Method area square calculation"""
        return self.__size**2
    def my_print(self):
        """Method print Square area"""
        if self.__size == 0:
            print("")
        else:
            for x in range(self.size):
                if self.position[1] >= 0:
                    for i in range(self.position[0]):
                        print(" ", end='')
                for y in range(self.size):
                    print("#", end='')
                print("")
    def __str__(self):
        """str method"""
        if self.__size == 0:
            return ""
        else:
            if self.position[1] >= 0:
                space = " " * self.position[0]
            else:
                space = ""
            hash = "#" * self.size
        return "\n".join(space + hash for i in range(self.size))
