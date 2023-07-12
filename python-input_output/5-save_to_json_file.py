#!/usr/bin/python3
""" json modules"""
import json


def save_to_json_file(my_obj, filename):
    """saves a json file"""
    with open(filename, "w")as f:
        json.dump(my_obj, f)
