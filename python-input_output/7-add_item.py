#!/usr/bin/python3
"""module"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
file = "add_item.json"
arguments = sys.argv[1:]
try:
    data = load_from_json_file(file)
except FileNotFoundError:
    data = []
data.extend(arguments)
save_to_json_file(data, file)
