#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for innerlist in matrix:
        for element in innerlist:
            print(element, end=",")
        print()
