#!/usr/bin/python3
class Square:
    def __init__(self, ssize=0):
        try:
            self.__size = ssize
            if ssize < 0:
                raise Exception("size must be >= 0")
        except TypeError:
            raise Exception("size must be an integer")
    def area(self):
        return self.__size**2
