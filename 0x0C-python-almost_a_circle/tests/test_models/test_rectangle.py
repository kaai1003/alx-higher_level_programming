#!/usr/bin/python3
"""unittest Rectangle Class module"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """UnitTest Rectangle Class Module"""

    def test_new_Rectangle(self):
        """test different attributes"""

        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 12)
        r2 = Rectangle("a", "b", "c", "d", 13)
        self.assertEqual(r2.width, "a")
        self.assertEqual(r2.height, "b")
        self.assertEqual(r2.x, "c")
        self.assertEqual(r2.y, "d")
        self.assertEqual(r2.id, 13)

    def test_r_args(self):
        """test number args passed to Rectangle"""

        r3 = Rectangle(10, 2)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r3.id, 1)
        r4 = Rectangle(10, 2, 14)
        self.assertEqual(r4.width, 10)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 14)
        self.assertEqual(r4.y, 0)
        self.assertEqual(r4.id, 2)
        r5 = Rectangle(10, 2, 14, 4)
        self.assertEqual(r5.width, 10)
        self.assertEqual(r5.height, 2)
        self.assertEqual(r5.x, 14)
        self.assertEqual(r5.y, 4)
        self.assertEqual(r5.id, 3)
        with self.assertRaises(TypeError):
            r6 = Rectangle(7)
        with self.assertRaises(TypeError):
            r7 = Rectangle()
