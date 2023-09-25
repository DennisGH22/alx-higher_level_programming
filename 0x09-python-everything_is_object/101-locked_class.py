#!/usr/bin/python3
"""
A class that restricts the creation of new instance attributes,
except for 'first_name'.
"""


class LockedClass:
    """
    A class that restricts the creation of new instance attributes,
    except for 'first_name'.
    """

    __slots__ = ('first_name',)
