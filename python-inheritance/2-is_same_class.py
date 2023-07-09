#!/usr/bin/python3
"""
module that checks if object is exactly
an instance of a specified class

"""


def is_same_class(obj, a_class):
    """
    checks
    """
    if type(obj) is a_class:
        return True
    else:
        return False
