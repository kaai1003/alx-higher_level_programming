#!/usr/bin/python3
""" 4-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6, 3, 3)
    r1.display()

    print("---")

    r1 = Rectangle(2, 4, 2, 0)
    r1.display()