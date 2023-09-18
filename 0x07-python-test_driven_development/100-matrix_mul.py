#!/usr/bin/python3
""" Multiply two matrices. """


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    :param m_a: The first matrix as a list of lists of integers or floats.
    :param m_b: The second matrix as a list of lists of integers or floats.
    :return: The result of matrix multiplication as a new matrix.
    :raises TypeError: If m_a or m_b is not a list, not a list of lists,
                       empty, or contains non-integer/float elements.
    :raises ValueError: If m_a and m_b cannot be multiplied.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if (
        not all(isinstance(num, (int, float))
                for row in m_a for num in row)
    ):
        raise TypeError("m_a should contain only integers or floats")

    if (
        not all(isinstance(num, (int, float))
                for row in m_b for num in row)
    ):
        raise TypeError("m_b should contain only integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")

    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
