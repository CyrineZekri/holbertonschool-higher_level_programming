#!/usr/bin/python3
"""
module that contains functions related to python Inheritance.


"""


class MyList(list):
    """
    class that defines a list
    """

    def print_sorted(self):
        sorted_list = sorted(self)
        print("[", end="")
        for i in range(len(sorted_list)):
            if i == len(sorted_list) - 1:
                print(sorted_list[i], end="")
            else:
                print(sorted_list[i], end=", ")
        print("]\n", end="")
