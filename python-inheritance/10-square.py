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
        super().__init__("size", size)
        self.__size = size

    def area(self):
        """
        method to calculate the area
        """
        return self.__size * self.__size
