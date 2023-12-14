#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position
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
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    def area(self):
        return self.__size**2
    def my_print(self):
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
