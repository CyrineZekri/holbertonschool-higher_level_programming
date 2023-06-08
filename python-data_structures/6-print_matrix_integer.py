#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    for innerlist in matrix:
        for element in innerlist:
            print(element, end=",")
        print()
