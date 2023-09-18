#!/usr/bin/python3
""" Divide all elements of a matrix by a divisor. """


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor.

    :param matrix: A list of lists containing integers or floats.
    :param div: A number (integer or float) to divide the elements by.
    :return: A new matrix with elements divided by the divisor
             rounded to 2 decimal places.
    :raises TypeError: If matrix is not a list of lists of integers/floats,
                       if each row of the matrix does not have the same size,
                       if div is not a number (integer or float).
    :raises ZeroDivisionError: If div is equal to zero (division by zero).
    """
    if (
        not isinstance(matrix, list)
        or not all(isinstance(row, list)
                   and all(isinstance(num, (int, float))
                           for num in row) for row in matrix)
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    if any(len(row) != row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    results = [[round(num / div, 2) for num in row] for row in matrix]

    return results
