#!/usr/bin/python3
""" Module with the Base model"""
import json


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """JSON representation"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return (json.dumps(list_dictionaries))
