#!/usr/bin/python3
"""

module that contains the function : text_indentation

"""


def text_indentation(text):
    """
    indents text after special characters
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    characters = ['.', '?', ':']
    returned = ""
    for i, char in enumerate(text):
        returned += char
        if char in characters and i < len(text)-1:
            returned += "\n\n"
    print(returned)
