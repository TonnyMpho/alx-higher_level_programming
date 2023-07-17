#!/usr/bin/python3
"""
Unittest for the Base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Unittest class """
    def test_id(self):
        """
        Test initializing an instance of Base class with id > 0
        """
        b = Base(12)
        self.assertEqual(12, b.id)

    def test_id_zero(self):
        """
        Test initializing an instance of Base class with id == 0
        """
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):
        """
        Test initializing an instance of Base class with id < 0
        """
        b = Base(-2)
        self.assertEqual(-2, b.id)

    def test_id_string(self):
        """
        Test initializing an instance of Base class with id as string
        """
        b = Base("Base")
        self.assertEqual("Base", b.id)

    def test_id_list(self):
        """
        Test initializing an instance of Base class with id as list
        """
        b = Base([1, 3, 6])
        self.assertEqual([1, 3, 6], b.id)

    def test_id_tuple(self):
        """
        Test initializing an instance of Base class with id as tuple
        """
        b = Base((1, 3))
        self.assertEqual((1, 3), b.id)

    def test_id_dict(self):
        """
        Test initializing an instance of Base class with id as dict
        """
        b = Base({'id': 12})
        self.assertEqual({'id': 12}, b.id)

    def test_to_json_string(self):
        """
        Test to_json_string method with list of dictionaries
        """
        b = Base()
        json_string = b.to_json_string(
                [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}])
        self.assertEqual(
                '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]',
                json_string)

    def test_from_json_string(self):
        """
        Test from_json_string method with a valid JSON string
        """
        b = Base()
        json_string = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        json_list = b.from_json_string(json_string)
        self.assertEqual(
                [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}],
                json_list)


if __name__ == '__main__':
    unittest.main()
