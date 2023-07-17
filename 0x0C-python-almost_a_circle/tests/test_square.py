#!/usr/bin/python3
""" Unittest for the square """
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Unittest class """
    def test_size(self):
        """
        Test getter and setter for size attribute
        """
        s = Square(10)
        self.assertEqual(10, s.size)

        s.size = 20
        self.assertEqual(20, s.size)

        with self.assertRaises(TypeError):
            s.size = "string"

        with self.assertRaises(ValueError):
            s.size = -5

    def test_x(self):
        """
        Test getter and setter for x attribute
        """
        s = Square(10, 2, 3)
        self.assertEqual(2, s.x)

        s.x = 5
        self.assertEqual(5, s.x)

        with self.assertRaises(TypeError):
            s.x = "string"

        with self.assertRaises(ValueError):
            s.x = -2

    def test_y(self):
        """
        Test getter and setter for y attribute
        """
        s = Square(10, 2, 3)
        self.assertEqual(3, s.y)

        s.y = 4
        self.assertEqual(4, s.y)

        with self.assertRaises(TypeError):
            s.y = "string"

        with self.assertRaises(ValueError):
            s.y = -1

    def test_area(self):
        """
        Test area method
        """
        s = Square(10)
        self.assertEqual(100, s.area())

        s.size = 8
        self.assertEqual(64, s.area())

    def test_display(self):
        """
        Test display method
        """
        s = Square(4, 2, 1)
        s.display()

    def test_str(self):
        """
        Test __str__ method
        """
        s = Square(6, 2, 1, 9)
        self.assertEqual("[Square] (9) 2/1 - 6", str(s))

    def test_update(self):
        """
        Test update method with *args
        """
        s = Square(10)
        s.update(1, 2, 3, 4)
        self.assertEqual("[Square] (1) 3/4 - 2", str(s))

    def test_update_kwargs(self):
        """
        Test update method with **kwargs
        """
        s = Square(10)
        s.update(id=1, size=2, x=3, y=4)
        self.assertEqual("[Square] (1) 3/4 - 2", str(s))

    def test_update_both(self):
        """
        Test update method with both *args and **kwargs
        """
        s = Square(10)
        s.update(1, **{'size': 2, 'x': 3, 'y': 4})
        self.assertEqual("[Square] (1) 0/0 - 10", str(s))

    def test_to_dictionary(self):
        """
        Test to_dictionary method
        """
        s = Square(10, 2, 1, 9)
        self.assertEqual(
                {'id': 9, 'x': 2, 'size': 10, 'y': 1}, s.to_dictionary())


if __name__ == '__main__':
    unittest.main()
