#!/usr/bin/python3
""" Module Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Class constructor """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ public getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ public setter for size """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        public method update *args, **kwargs that assigns attributes:
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            keys = ['id', 'size', 'x', 'y']
            for key, val in kwargs.items():
                if key in keys:
                    setattr(self, key, val)

    def to_dictionary(self):
        """
        public method that returns the dictionary representation
        of a Square
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}

    def __str__(self):
        """ string representaion of a Square """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)
