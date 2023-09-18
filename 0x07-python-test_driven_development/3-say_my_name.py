#!/usr/bin/python3
""" Print a message with the first name and last name. """


def say_my_name(first_name, last_name=""):
    """
    Print a message with the first name and last name.

    :param first_name: The first name (a string).
    :param last_name: The last name (optional, a string).
    :raises TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
