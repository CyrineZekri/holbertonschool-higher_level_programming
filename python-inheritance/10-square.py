#!/usr/bin/python3
'''
Square module
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    square rectangle
    """

    def __init__(self, size):
        """
        instanciation method
        """
        self.integer_validator("size", size)
        self._Rectangle__width = size
        self._Rectangle__height = size
        self.__size = size

    def area(self):
        """
        method to calculate the area
        """
        return self.__size**2
