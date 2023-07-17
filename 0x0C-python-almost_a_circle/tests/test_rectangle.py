#!/usr/bin/python3
"""
Unittest for the Rectangle model
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Unittest """
    def test_width(self):
        """
        Test getter and setter for width attribute
        """
        r = Rectangle(10, 5)
        self.assertEqual(10, r.width)

        r.width = 20
        self.assertEqual(20, r.width)

        with self.assertRaises(TypeError):
            r.width = "string"

        with self.assertRaises(ValueError):
            r.width = -5

    def test_height(self):
        """
        Test getter and setter for height attribute
        """
        r = Rectangle(10, 5)
        self.assertEqual(5, r.height)

        r.height = 8
        self.assertEqual(8, r.height)

        with self.assertRaises(TypeError):
            r.height = "string"

        with self.assertRaises(ValueError):
            r.height = -3

    def test_x(self):
        """
        Test getter and setter for x attribute
        """
        r = Rectangle(10, 5, 2, 3)
        self.assertEqual(2, r.x)

        r.x = 5
        self.assertEqual(5, r.x)

        with self.assertRaises(TypeError):
            r.x = "string"

        with self.assertRaises(ValueError):
            r.x = -2

    def test_y(self):
        """
        Test getter and setter for y attribute
        """
        r = Rectangle(10, 5, 2, 3)
        self.assertEqual(3, r.y)

        r.y = 4
        self.assertEqual(4, r.y)

        with self.assertRaises(TypeError):
            r.y = "string"

        with self.assertRaises(ValueError):
            r.y = -1

    def test_area(self):
        """
        Test area method
        """
        r = Rectangle(10, 5)
        self.assertEqual(50, r.area())

        r.width = 8
        r.height = 7
        self.assertEqual(56, r.area())

    def test_display(self):
        """
        Test display method
        """
        r = Rectangle(3, 2, 1, 1)
        r.display()

    def test_str(self):
        """
        Test __str__ method
        """
        r = Rectangle(4, 6, 2, 1, 9)
        self.assertEqual("[Rectangle] (9) 2/1 - 4/6", str(r))

    def test_update(self):
        """
        Test update method with *args
        """
        r = Rectangle(10, 5)
        r.update(1, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (1) 4/5 - 2/3", str(r))

    def test_update_kwargs(self):
        """
        Test update method with **kwargs
        """
        r = Rectangle(10, 5)
        r.update(id=1, width=2, height=3, x=4, y=5)
        self.assertEqual("[Rectangle] (1) 4/5 - 2/3", str(r))

    def test_update_both(self):
        """
        Test update method with both *args and **kwargs
        """
        r = Rectangle(10, 5)
        r.update(1, 2, 3, **{'x': 4, 'y': 5})
        self.assertEqual("[Rectangle] (1) 0/0 - 2/3", str(r))

    def test_to_dictionary(self):
        """
        Test to_dictionary method
        """
        r = Rectangle(10, 5, 2, 1, 9)
        self.assertEqual({'x': 2, 'y': 1, 'id': 9, 'height': 5, 'width': 10}, r.to_dictionary())


if __name__ == '__main__':
    unittest.main()
