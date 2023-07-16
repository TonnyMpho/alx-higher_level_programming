#!/usr/bin/python3
""" Module class Rectangle """
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor
        Private instance attributes, each with its own public
        getter and setter. Call the super class with id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        private attributes width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ private attributes width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
        private attributes height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ private attributes height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        private attributes x getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ private attributes x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ private attributes y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ private attributes y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        public method area that returns the area
        value of the Rectangle instance.
        """
        return self.width * self.height

    def display(self):
        """
        public method that prints in stdout the Rectangle
        instance with the character #
        """
        for i in range(self.y):
            print()

        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """
        public method update that assigns an argument to each attribute
        using `*args` and `**kwargs`
        """
        if args:
            for i, val in enumerate(args):
                if i == 0:
                    self.id = val
                if i == 1:
                    self.width = val
                if i == 2:
                    self.height = val
                if i == 3:
                    self.x = val
                if i == 4:
                    self.y = val
        elif kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """
        public method that returns the dictionary representation
        of a Rectangle
        """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}

    def __str__(self):
        """
        method that returns the string representation of a class
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)
