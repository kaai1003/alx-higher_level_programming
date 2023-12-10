#!/usr/bin/python3
class Square:
    def __init__(self, ssize=0):
        self.size = ssize
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise Exception("size must be an integer")
        elif value < 0:
            raise Exception("size must be >= 0")
        else:
            self.__size = value
    def area(self):
        return self.__size**2
