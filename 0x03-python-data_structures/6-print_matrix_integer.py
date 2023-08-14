#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    print('\n'.join([' '.join(['{:2}'.format(j) for j in i]) for i in matrix]))
