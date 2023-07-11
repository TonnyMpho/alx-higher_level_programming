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
        self.firt_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Public method that retrieves a dictionary
        representation of a Student instance
        """
        return self.__dict__
