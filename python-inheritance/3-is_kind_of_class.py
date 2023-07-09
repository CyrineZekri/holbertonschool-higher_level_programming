#!/usr/bin/python3
"""
module to check if an object is
an instance of a class or a class
that inhereited from
"""


def is_kind_of_class(obj, a_class):
    """"
    checks
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
