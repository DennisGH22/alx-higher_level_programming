#!/usr/bin/python3
"""This class representing a node in a singly linked list."""


class Node:
    """This class representing a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """
        Initialize a Node with data and an optional next_node.

        :param data: Integer data for the node.
        :param next_node: The next node in the linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node."""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This class representing a node in a singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the list.

        :param value: Integer value to be inserted.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """
        Generate a string representation of the linked list.

        :return: String representation of the linked list.
        """
        values = [str(node.data) for node in self]
        return '\n'.join(values)

    def __iter__(self):
        """Make the linked list iterable."""
        current = self.__head
        while current:
            yield current
            current = current.next_node
