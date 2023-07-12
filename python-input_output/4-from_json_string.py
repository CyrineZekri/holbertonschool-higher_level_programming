#!/usr/bin/python3
"""deserializaton json"""
import json

def from_json_string(my_str):
    """decodes a json string to obj"""
    return json.loads(my_str)