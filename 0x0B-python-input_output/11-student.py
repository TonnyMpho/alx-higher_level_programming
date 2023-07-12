#!/usr/bin/python3
""" Module that defines the class Student """


class Student:
    """
    class Student that defines a student by
    """
    def __init__(self, first_name, last_name, age):
        """
        Public instance attributes: first_name last_name age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public method that retrieves a dictionary
        representation of a Student instance
        """
        attr_dict = {}
        if attrs is not None and isinstance(attrs, list):
            for attr in attrs:
                if isinstance(attr, str) and hasattr(self, attr):
                    attr_dict[attr] = getattr(self, attr)
            return attr_dict

        return self.__dict__

    def reload_from_json(self, json):
        """
        Public method that replaces all
        attributes of the Student instance
        """
        for key, value in json.items():
            setattr(self, key, value)
