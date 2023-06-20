#!/usr/bin/python3
"""

module that contains the function : text_indentation



"""


def text_indentation(text):
    """
    indents after special characters
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    tmp = text.replace(".", ".\n\n")
    tmp = tmp.replace(":", ":\n\n")
    tmp = tmp.replace("?", "?\n\n")
    p = tmp.splitlines(True)
    ls_strip = []
    for l in p:
        if l == "\n":
            ls_strip.append("\n")
        else:
            ls_strip.append(l.lstrip())
    print("".join(ls_strip), end="")
