#!/usr/bin/python3
"""unittest Base Class module"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """UnitTest Base Class Module"""

    def test_id(self):
        """test different value of id"""

        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(23)
        self.assertEqual(b3.id, 23)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_nb_args(self):
        """test number args passed to Base"""

        b1 = Base()
        self.assertEqual(b1.id, 4)
        b2 = Base(23)
        self.assertEqual(b2.id, 23)
        with self.assertRaises(TypeError):
            b3 = Base(7, 10)
