#!/usr/bin/python3
""" This class represents a square. """


class Square:
    """ This class represents a square. """

    def __init__(self, size=0):
        """
        Initialize a new Square object with a specified size.

        Args:
            size (int or float): The size of the square's sides (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int or float): The size of the square's sides.

        Raises:
            TypeError: If the value is not a number (int or float).
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compare if two Square objects have equal areas.

        Args:
            other (Square): The other Square object to compare.

        Returns:
            bool: True if areas are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Compare if two Square objects have unequal areas.

        Args:
            other (Square): The other Square object to compare.

        Returns:
            bool: True if areas are unequal, False otherwise.
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        Compare if one Square has a greater area than the other.

        Args:
            other (Square): The other Square object to compare.

        Returns:
            bool: True if the area is greater, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """
        Compare if one Square has a greater or equal area than the other.

        Args:
            other (Square): The other Square object to compare.

        Returns:
            bool: True if the area is greater or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __lt__(self, other):
        """
        Compare if one Square has a smaller area than the other.

        Args:
            other (Square): The other Square object to compare.

        Returns:
            bool: True if the area is smaller, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """
        Compare if one Square has a smaller or equal area than the other.

        Args:
            other (Square): The other Square object to compare.

        Returns:
            bool: True if the area is smaller or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False
