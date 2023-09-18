#!/usr/bin/python3
""" Base class for managing unique identifiers. """


class Base:
    """
    Base class for managing unique identifiers.

    This class serves as the base for all other classes in the project.
    It manages the 'id' attribute to ensure each instance
    has a unique identifier.

    Attributes:
        __nb_objects (int): A private class attribute to count the number
        of objects reated from this class.

    Methods:
        __init__(self, id=None):
            Constructor for the Base class.
            Initializes the 'id' attribute either with
            the provided 'id' argument or assigns a unique identifier.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance.

        Args:
            id (int, optional): An optional integer identifier.
            If provided, it will be assigned as the 'id' attribute.
            If not provided, a unique identifier will be generated.

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
