#!/usr/bin/python3
import numpy as np

""" Multiply two matrices using NumPy. """


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    :param m_a: The first matrix as a NumPy array.
    :param m_b: The second matrix as a NumPy array.
    :return: The result of matrix multiplication as a NumPy array.
    :raises ValueError: If the matrices cannot be multiplied.
    """
    result = np.matmul(m_a, m_b)
    return result
