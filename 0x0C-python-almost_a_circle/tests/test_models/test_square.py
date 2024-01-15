#!/usr/bin/python3
"""unittest Square Class module"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.square import Square


class TestSquare(unittest.TestCase):
    """UnitTest Square Class Module"""
    def test_new_Square(self):
        """test normal integer attributes"""

        s1 = Square(2, 0, 0, 12)
        self.assertEqual(s1.width, 2)
        self.assertEqual(s1.height, 2)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 12)

    def test_type_attributes(self):
        """test type attributes"""

        with self.assertRaises(TypeError) as msg:
            s1 = Square("a")
        self.assertEqual(str(msg.exception), "width must be an integer")
        with self.assertRaises(TypeError) as msg:
            s1 = Square(7, '0', 0)
        self.assertEqual(str(msg.exception), "x must be an integer")
        with self.assertRaises(TypeError) as msg:
            s1 = Square(7, 0, '0')
        self.assertEqual(str(msg.exception), "y must be an integer")

    def test_range_attributes(self):
        """test range of attributes"""

        with self.assertRaises(ValueError) as msg:
            s1 = Square(0)
        self.assertEqual(str(msg.exception), "width must be > 0")
        with self.assertRaises(ValueError) as msg:
            s1 = Square(-3)
        self.assertEqual(str(msg.exception), "width must be > 0")
        with self.assertRaises(ValueError) as msg:
            s1 = Square(7, -2, 0)
        self.assertEqual(str(msg.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as msg:
            s1 = Square(7, 0, -2)
        self.assertEqual(str(msg.exception), "y must be >= 0")

    def test_square_args(self):
        """test number args passed to Square"""

        s1 = Square(10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 5)
        s1 = Square(10, 14)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 14)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 6)
        s1 = Square(10, 2, 14, 4)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 14)
        self.assertEqual(s1.id, 4)
        with self.assertRaises(TypeError):
            s1 = Square()

    def test_area_method(self):
        """test area Method calculation"""

        s1 = Square(2)
        self.assertEqual(s1.area(), 4)
        with self.assertRaises(ValueError) as msg:
            s1 = Square(-2)
            s1.area()
        self.assertEqual(str(msg.exception), "width must be > 0")

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_method(self, stdout):
        """test Square representation display"""

        s1 = Square(2)
        s1.display()
        self.assertEqual(stdout.getvalue(), "##\n" * 2)

    @patch('sys.stdout', new_callable=StringIO)
    def test_str_method(self, stdout):
        """test str method"""
        s1 = Square(4, 2, 4, 30)
        print(s1)
        self.assertEqual(stdout.getvalue(), "[Square] (30) 2/4 - 4\n")

    def test_update_method_args(self):
        """test update method with args"""

        s1 = Square(10, 10, 10, 10)
        s1.update(89)
        self.assertEqual(s1.id, 89)

        s1.update(89, 2)
        self.assertEqual(s1.width, 2)

        s1.update(89, 2, 3)
        self.assertEqual(s1.height, 2)

        s1.update(89, 2, 3, 4)
        self.assertEqual(s1.x, 3)

        s1.update(89, 2, 3, 5)
        self.assertEqual(s1.y, 5)

    def test_update_method_kwargs(self):
        """test update method with kwargs"""

        s1 = Square(10, 10, 10, 10)

        s1.update(size=1)
        self.assertEqual(s1.height, 1)

        s1.update(width=1, x=2)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.x, 2)

        s1.update(y=1, size=2, x=3, id=89)
        self.assertEqual(s1.width, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 1)
        self.assertEqual(s1.id, 89)

        s1.update(x=1, size=4, y=3)
        self.assertEqual(s1.width, 4)
        self.assertEqual(s1.height, 4)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 3)

    def test_size_square(self):
        """test size square"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(s1.size, 10)
        with self.assertRaises(TypeError) as msg:
            s1.size = "b"
        self.assertEqual(str(msg.exception), "width must be an integer")
        with self.assertRaises(ValueError) as msg:
            s1.size = -1
        self.assertEqual(str(msg.exception), "width must be > 0")

    def test_dict_repr(self):
        """test dict repr of rectangle"""
        s1 = Square(10, 2, 1)
        dict_s1 = s1.to_dictionary()
        self.assertEqual(dict_s1, {'id': 2,
                                   'x': 2,
                                   'size': 10,
                                   'y': 1})
        self.assertEqual(str(type(dict_s1)), "<class 'dict'>")


if __name__ == "__main__":
    unittest.main()
