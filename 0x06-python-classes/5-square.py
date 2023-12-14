#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size
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
    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for x in range(self.size):
                for y in range(self.size):
                    print("#", end='')
                print("")
