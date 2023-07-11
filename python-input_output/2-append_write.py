#!/usr/bin/python3
"""append writes in a file"""


def append_write(filename="", text=""):
    """appends to file"""
    with open(filename, "a", encoding="UTF8") as f:
        f.write(text)
    return len(text)
