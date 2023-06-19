#!/usr/bin/python3
"""
module that contains the function : text_indentation
"""


def text_indentation(text):
    """
    indents two lines after :  . ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    characters = ['.', '?', ':']
    returned = ""
    for char in text:
        returned += char
        if char in characters:
            returned += "\n\n"
    print(returned.strip())
