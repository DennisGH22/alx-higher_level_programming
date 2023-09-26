#!/usr/bin/python3
"""
Check if an object is an instance of a class
that inherited from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class
    that is inherited from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a class
        that is inherited from a_class, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
