#!/usr/nin/python3
""" the “base” of all other classes in this project """
import json
import os


class Base:
    """
    the first class
    base class of all other clasess
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor - if id is not None, assign the
        public instance attribute id with this argument value
        otherwise, increment __nb_objects and assign the new
        value to the public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        static method that returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method that writes the JSON string representation
        of list_objs to a file
        """
        filename = cls.__name__ + '.json'
        if list_objs is None:
            list_objs = []

        with open(filename, 'w', encoding='utf-8') as f:
            dictionary = []
            for obj in list_objs:
                dictionary.append(obj.to_dictionary())
            f.write(cls.to_json_string(dictionary))

    @staticmethod
    def from_json_string(json_string):
        """
        static method that returns the list of the
        JSON string representation json_string:
        """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        class method that returns an instance with all
        attributes already set:
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + '.json'
        instances = []

        if os.path.isfile(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                json_str = cls.from_json_string(f.read())

                for ins in json_str:
                    instances.append(cls.create(**ins))
                return instances
        return instances
