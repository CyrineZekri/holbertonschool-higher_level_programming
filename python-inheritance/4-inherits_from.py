#!/usr/bin/python3
"""
module that checks for
inheritance links

"""


def inherits_from(obj, a_class):
    """
    checks
    """
    if isinstance(object, a_class):
        return True
    if issubclass(type(obj), a_class) and not isinstance(obj, a_class):
        return True
