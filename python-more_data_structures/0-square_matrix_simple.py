#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for i in range(len(matrix)):
        tmp = []
        for j in range(len(matrix[i])):
            tmp.append(matrix[i][j] ** 2)
        result.append(tmp)
    return result
