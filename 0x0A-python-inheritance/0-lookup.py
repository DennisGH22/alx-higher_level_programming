#!/usr/bin/python3
"""Return a list of available attributes and methods of an object."""


def lookup(obj):
    """
    Return a list of available attributes and methods of an object.

    Args:
        obj: The object for which to retrieve attributes and methods.

    Returns:
        List of attribute and method names.
    """
    return dir(obj)
