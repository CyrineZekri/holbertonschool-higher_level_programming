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

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON representation"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON repr to a file"""
        if list_objs is None:
            list_objs = []
        for inst in list_objs:
            element = inst.to_dictionary()
        with open(f"{cls.__name__}.json", "w") as f:
            f.write(cls.to_json_string(element))
