#!/usr/bin/python3
"""A custom list class that inherits from the built-in list class."""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    Attributes:
        Inherits all attributes and methods from the built-in list class.
    """

    def print_sorted(self):
        """
        Print the elements of the list in ascending sorted order.

        Sorts the elements of the list in ascending order and prints them.
        """
        sorted_list = sorted(self)
        print(sorted_list)
