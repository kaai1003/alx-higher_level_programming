#!/usr/bin/python3
"""MagiscClass Class"""
import math
class MagicClass():
    """MagicClass Class definition
    Atrributes:
        radius: radius value
    """
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) != int and type(radius) != float:
            raise TypeError("radius must be a number")
        self.__radius = radius
    def area(self):
        """define area
        """
        return (self.__radius ** 2) * math.pi
    
    def circumference(self):
        """circumference Method
        """
        return 2 * math.pi * self.__radius
