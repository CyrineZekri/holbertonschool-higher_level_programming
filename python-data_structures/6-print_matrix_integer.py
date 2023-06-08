#!/usr/bin/env python3

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def print_matrix_integer(matrix=[[]]):

    for innerlist in matrix:
        for element in innerlist:
            print(element, end=",")
        print()
