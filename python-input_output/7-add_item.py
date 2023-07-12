#!/usr/bin/python3
"""module"""
import sys
if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__(
        '6-loads_from_json_file').load_from_json_file
    file = "add_item.json"
    args = sys.argv[1:]
    try:
        list = load_from_json_file(file)
    except FileNotFoundError:
        list = []
    list.extend(args)
    save_to_json_file(list)
