#!/usr/bin/python3
"""
Module add_integer: Contains a function to add two int or float numbers.
"""


def add_integer(a, b=98):
    """
    Function that adds two int or float numbers
       Raises a TypeError if a or b is not an integer or float.
       Returns the sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a+b)
