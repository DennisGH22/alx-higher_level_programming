#!/usr/bin/python3
""" Add two integers. """


def add_integer(a, b=98):
    """
    Add two integers.

    :param a: An integer or a float to be added.
    :param b: An integer or a float to be added. Defaults to 98.
    :return: The addition of a and b as an integer.
    :raises TypeError: If a or b is not an integer or a float.
    """
    if not (isinstance(a, (int, float))):
        raise TypeError("a must be an integer")

    if not (isinstance(b, (int, float))):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    result = a + b

    return result
