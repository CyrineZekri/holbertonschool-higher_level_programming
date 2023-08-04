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
        if list_objs is None or list_objs == []:
            list_objs = []
        with open(f"{cls.__name__}.json", "w") as f:
            list_instances = []
            for i in range(len(list_objs)):
                inst = list_objs[i]
                inst_dic = inst.to_dictionary()
                list_instances.append(inst_dic)
            final = cls.to_json_string(list_instances)
            f.write(final)

    @staticmethod
    def from_json_string(json_string):
        """reloads the list of dictionaries from a file"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
