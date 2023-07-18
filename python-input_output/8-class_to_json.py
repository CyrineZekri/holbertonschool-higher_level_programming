#!/usr/bin/python3
""" module that returns representations"""


def class_to_json(obj):
    dictionary = obj.__dict__
    return dictionary
