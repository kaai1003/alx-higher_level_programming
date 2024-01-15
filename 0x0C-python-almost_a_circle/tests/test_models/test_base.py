#!/usr/bin/python3
"""unittest Base Class module"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


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
        self.assertEqual(b1.id, 5)
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
                                      'id': 4,
                                      'height': 7,
                                      'width': 10})
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, str([{'x': 2,
                                                'y': 8,
                                                'id': 4,
                                                'height': 7,
                                                'width': 10}]))

    def test_save_tofile(self):
        """test save to file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), [{"x": 2, "y": 8, "id": 1,
                                            "height": 7, "width": 10},
                                           {"x": 0, "y": 0, "id": 2,
                                            "height": 4, "width": 2}])


if __name__ == "__main__":
    unittest.main()
