#!/usr/bin/python3
class Square:
    def __init__(self, ssize=0):
        self.__size = ssize
        if type(ssize) != int:
            raise Exception("size must be an integer")
        elif ssize < 0:
            raise Exception("size must be >= 0")
