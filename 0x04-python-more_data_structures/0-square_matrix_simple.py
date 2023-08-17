#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    for i in matrix:
        squared_matrix = []
        for j in i:
            squared_matrix.append(j ** 2)
        new_matrix.append(squared_matrix)

    return new_matrix
