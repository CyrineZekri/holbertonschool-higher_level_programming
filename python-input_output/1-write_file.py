#!/usr/bin/python3
"""writes in a file"""


def write_file(filename="", text=""):
    """writes to a file"""
    with open(filename, "w", encoding="UTF8") as f:
        f.write(text)
        return len(text)
