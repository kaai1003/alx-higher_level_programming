#!/usr/bin/python3
"""unittest module"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """UnitTest Class"""

    def test_integer(self):
        """test list of integers"""

        list = [1, 3, 6, 9]
        self.assertEqual(max_integer(list), 9)
        list = [9, 3, 6, 1]
        self.assertEqual(max_integer(list), 9)
        list = [4]
        self.assertEqual(max_integer(list), 4)

    def test_emptylist(self):
        """test empty list"""

        list = []
        self.assertEqual(max_integer(list), None)

    def test_float_list(self):
        """test list of floats"""

        list = [1.5, 0.5, 3.4, 1]
        self.assertEqual(max_integer(list), 3.4)

    def test_str_list(self):
        """test list contains strings"""

        list = [3, "b", 5]
        self.assertRaises(TypeError)
        list = ["e", "s", "t", "a"]
        self.assertEqual(max_integer(list), "t")
