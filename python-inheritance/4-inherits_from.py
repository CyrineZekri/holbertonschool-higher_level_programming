#!/usr/bin/python3
"""
module that checks for
inheritance links

"""


def inherits_from(obj, a_class):
    """
    checks
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class
