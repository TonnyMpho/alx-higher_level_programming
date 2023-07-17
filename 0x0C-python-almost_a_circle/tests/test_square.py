#!/usr/bin/python3
"""Unittests for base
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Define unit test for Square model"""

    def test_initialization(self):
        s1 = Square(5)
        s2 = Square(2, 2)
        self.assertEqual(s1, '[Square] (1) 0/0 - 5')
        self.assertEqual(s2, '[Square] (2) 2/0 - 2')
        self.assertRaises(TypeError, Square)

if __name__ == '__main__':
    unittest.main()
