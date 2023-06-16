#!/usr/bin/python3
"""Define an square with size class and functions"""


class Square:
    """Define a private attribute"""
    __size = None
    __position = None

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        if type(position) != tuple or (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for i in range(self.__size):
                    print('#' * self.__size)
            else:
                for i in range(self.__size):
                    print(" " * self.__position[0] + "#"*self.__size)
