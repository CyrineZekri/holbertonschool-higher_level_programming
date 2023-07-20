#!/usr/bin/python3
"""module that creates a triangle repr"""


def pascal_triangle(n):
    """function """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) < n:
        prev_row = triangle[-1]
        new_row = [1] + [prev_row[i] + prev_row[i + 1]
                         for i in range(len(prev_row) - 1)] + [1]
        triangle.append(new_row)

    return triangle
