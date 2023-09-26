#!/usr/bin/python3
"""BaseGeometry class."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Raise an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer value."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class, inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a Rectangle instance with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
