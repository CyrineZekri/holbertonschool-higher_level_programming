#!/usr/bin/python3
"""
geometry basics module
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
     class that inherits from BaseGeometry
    """

    def __init__(self, size):
        """
        intialize square
        """

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ area of square """

        return self.__size * self.__size
