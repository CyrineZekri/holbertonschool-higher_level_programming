#!/usr/bin/python3
""" json modules"""
import json


def load_from_json_file(filename):
    """ loads an object from a text file"""
    with open(filename, "r") as f:
        return json.load(f)
