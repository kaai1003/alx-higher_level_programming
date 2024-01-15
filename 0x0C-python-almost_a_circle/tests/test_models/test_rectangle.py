#!/usr/bin/python3
"""unittest Rectangle Class module"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """UnitTest Rectangle Class Module"""
    def test_new_Rectangle(self):
        """test normal integer attributes"""

        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 12)

    def test_type_attributes(self):
        """test type attributes"""

        with self.assertRaises(TypeError) as msg:
            r2 = Rectangle("a", 13)
        self.assertEqual(str(msg.exception), "width must be an integer")
        with self.assertRaises(TypeError) as msg:
            r2 = Rectangle(4, "13")
        self.assertEqual(str(msg.exception), "height must be an integer")
        with self.assertRaises(TypeError) as msg:
            r2 = Rectangle(7, 13, '0', 0)
        self.assertEqual(str(msg.exception), "x must be an integer")
        with self.assertRaises(TypeError) as msg:
            r2 = Rectangle(7, 13, 0, '0')
        self.assertEqual(str(msg.exception), "y must be an integer")

    def test_range_attributes(self):
        """test range of attributes"""

        with self.assertRaises(ValueError) as msg:
            r2 = Rectangle(0, 13)
        self.assertEqual(str(msg.exception), "width must be > 0")
        with self.assertRaises(ValueError) as msg:
            r2 = Rectangle(-3, 13)
        self.assertEqual(str(msg.exception), "width must be > 0")
        with self.assertRaises(ValueError) as msg:
            r2 = Rectangle(4, 0)
        self.assertEqual(str(msg.exception), "height must be > 0")
        with self.assertRaises(ValueError) as msg:
            r2 = Rectangle(4, -13)
        self.assertEqual(str(msg.exception), "height must be > 0")
        with self.assertRaises(ValueError) as msg:
            r2 = Rectangle(7, 13, -2, 0)
        self.assertEqual(str(msg.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as msg:
            r2 = Rectangle(7, 13, 0, -2)
        self.assertEqual(str(msg.exception), "y must be >= 0")

    def test_r_args(self):
        """test number args passed to Rectangle"""

        r3 = Rectangle(10, 2)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r3.id, 4)
        r4 = Rectangle(10, 2, 14)
        self.assertEqual(r4.width, 10)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 14)
        self.assertEqual(r4.y, 0)
        self.assertEqual(r4.id, 5)
        r5 = Rectangle(10, 2, 14, 4)
        self.assertEqual(r5.width, 10)
        self.assertEqual(r5.height, 2)
        self.assertEqual(r5.x, 14)
        self.assertEqual(r5.y, 4)
        self.assertEqual(r5.id, 6)
        with self.assertRaises(TypeError):
            r6 = Rectangle(7)
        with self.assertRaises(TypeError):
            r7 = Rectangle()

    def test_area_method(self):
        """test area Method calculation"""

        r1 = Rectangle(2, 5)
        self.assertEqual(r1.area(), 10)
        with self.assertRaises(ValueError) as msg:
            r1 = Rectangle(-2, 5)
            r1.area()
        self.assertEqual(str(msg.exception), "width must be > 0")

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_method(self, stdout):
        """test rectangle representation display"""

        r8 = Rectangle(2, 4)
        r8.display()
        self.assertEqual(stdout.getvalue(), "##\n" * 4)

    @patch('sys.stdout', new_callable=StringIO)
    def test_str_method(self, stdout):
        """test str method"""
        r9 = Rectangle(4, 6, 2, 4, 30)
        print(r9)
        self.assertEqual(stdout.getvalue(), "[Rectangle] (30) 2/4 - 4/6\n")

    def test_update_method_args(self):
        """test update method with args"""

        r10 = Rectangle(10, 10, 10, 10)
        r10.update(89)
        self.assertEqual(r10.id, 89)

        r10.update(89, 2)
        self.assertEqual(r10.width, 2)

        r10.update(89, 2, 3)
        self.assertEqual(r10.height, 3)

        r10.update(89, 2, 3, 4)
        self.assertEqual(r10.x, 4)

        r10.update(89, 2, 3, 4, 5)
        self.assertEqual(r10.y, 5)

    def test_update_method_kwargs(self):
        """test update method with kwargs"""

        r10 = Rectangle(10, 10, 10, 10)

        r10.update(height=1)
        self.assertEqual(r10.height, 1)

        r10.update(width=1, x=2)
        self.assertEqual(r10.width, 1)
        self.assertEqual(r10.x, 2)

        r10.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r10.width, 2)
        self.assertEqual(r10.x, 3)
        self.assertEqual(r10.y, 1)
        self.assertEqual(r10.id, 89)

        r10.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r10.width, 4)
        self.assertEqual(r10.height, 2)
        self.assertEqual(r10.x, 1)
        self.assertEqual(r10.y, 3)

    def test_dict_repr(self):
        """test dict repr of rectangle"""
        r1 = Rectangle(10, 2, 1, 9)
        dict_r1 = r1.to_dictionary()
        self.assertEqual(dict_r1, {'x': 1,
                                   'y': 9,
                                   'id': 2,
                                   'height': 2,
                                   'width': 10})
        self.assertEqual(str(type(dict_r1)), "<class 'dict'>")


if __name__ == "__main__":
    unittest.main()
