#!/usr/bin/python3
"""module"""
from models.base import Base


class Rectangle(Base):
    """rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """"constructeur"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area method"""
        return self.__height * self.__width

    def display(self):
        """method that represents a square using x and y for spaces """
        print('\n' * self.y, end='')
        print((' ' * self.x + '#' * self.width + '\n') * self.height, end='')

    def __str__(self):
        """The print method"""
        return f"[Rectangle] \
({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """method that adds arguments"""
        if args:
            arguments = len(args)
            if arguments >= 1:
                self.id = args[0]
            if arguments >= 2:
                self.width = args[1]
            if arguments >= 3:
                self.height = args[2]
            if arguments >= 4:
                self.x = args[3]
            if arguments >= 5:
                self.y = args[4]
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
