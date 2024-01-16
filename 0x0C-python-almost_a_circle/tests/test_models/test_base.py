#!/usr/bin/python3
"""unittest Base Class module"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """UnitTest Base Class Module"""
    def test_id(self):
        """test different value of id"""

        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(1)
        self.assertEqual(b2.id, 1)
        b3 = Base(23)
        self.assertEqual(b3.id, 23)
        b4 = Base()
        self.assertEqual(b4.id, 2)

    def test_nb_args(self):
        """test number args passed to Base"""

        b1 = Base()
        self.assertEqual(b1.id, 4)
        b2 = Base(23)
        self.assertEqual(b2.id, 23)
        with self.assertRaises(TypeError):
            b3 = Base(7, 10)

    def test_json_repr(self):
        """json string repr"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        self.assertEqual(dictionary, {'x': 2,
                                      'y': 8,
                                      'id': 3,
                                      'height': 7,
                                      'width': 10})
        json_dictionary = Rectangle.to_json_string([dictionary])
        dictionary = Rectangle.from_json_string(json_dictionary)
        self.assertEqual(dictionary, [{'x': 2,
                                       'y': 8,
                                       'id': 3,
                                       'height': 7,
                                       'width': 10}])

    def test_save_tofile_rect(self):
        """test save to file method for rectangle"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            list_rect = Rectangle.from_json_string(file.read())
            self.assertEqual(list_rect, [{"x": 2, "y": 8, "id": 5,
                                          "height": 7, "width": 10},
                                         {"x": 0, "y": 0, "id": 6,
                                          "height": 4, "width": 2}])

    def test_save_tofile_square(self):
        """test save to file method for square"""
        sq1 = Square(10, 7, 2, 8)
        sq2 = Square(2, 4, 3, 5)
        Square.save_to_file([sq1, sq2])

        with open("Square.json", "r") as file:
            list_rect = Square.from_json_string(file.read())
            self.assertEqual(list_rect, [{"id": 8, "x": 7,
                                          "size": 10, "y": 2},
                                         {"id": 5, "x": 4,
                                          "size": 2, "y": 3}])


if __name__ == "__main__":
    unittest.main()
