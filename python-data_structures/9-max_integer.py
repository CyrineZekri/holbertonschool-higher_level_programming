#!/usr/bin/python3
def max_integer(my_list=[]):
    x = len(my_list)
    max = my_list[0]
    for i in range(x - 1):
        if my_list[i] > max:
            max = my_list[i]
            return max
