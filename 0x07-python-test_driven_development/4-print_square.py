#!/usr/bin/python3
""" Print a square with the character '#' of the specified size. """


def print_square(size):
    """
    Print a square with the character '#' of the specified size.

    :param size: The size length of the square (an integer).
    :raises TypeError: If size is not an integer.
    :raises ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
            print("#" * size)
