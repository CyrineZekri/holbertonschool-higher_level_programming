#!/usr/bin/python3
'''
BaseGeometry module
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    Rectangle class that inherits from BaseGeometry
    '''

    def __init__(self, width, height):
        '''
        Instantiation of Rectangle class
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        returns area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        returns string representation
        """
        f"{Rectangle} <{self.__width}>/<{self.__height}>"
