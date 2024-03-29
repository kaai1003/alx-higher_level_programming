#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle
BaseGeometry = __import__('8-rectangle').BaseGeometry

r = Rectangle(3, 5)

print(r)
print(dir(r))
print(r.width)

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, "3")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

print(issubclass(Rectangle, BaseGeometry))