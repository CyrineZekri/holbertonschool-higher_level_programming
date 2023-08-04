#!/usr/bin/python3
"""Square module"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """method constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """representation method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    def update(self, *args, **kwargs):
        """the update method"""
        if args:
            arguments = len(args)
            if arguments >= 1:
                self.id = args[0]
            if arguments >= 2:
                self.width = args[1]
            if arguments >= 4:
                self.x = args[3]
            if arguments >= 5:
                self.y = args[4]
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """the dictionary representation """
        dic = {'id': self.id, 'x': self.x, 'size': self.width,  'y': self.y}
        return (dic)
