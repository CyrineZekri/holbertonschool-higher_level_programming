#!/usr/bin/python3
"""
module with geometry basics


"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    rectangle class
    """

    def __init__(self, width, height):
        self.integer_validator("height", width)
        self.integer_validator("height", height)
        self.__width__ = width
        self.__height__ = height
