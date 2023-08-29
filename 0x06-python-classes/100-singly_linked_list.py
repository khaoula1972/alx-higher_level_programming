#!/usr/bin/python3
"""
Class: Node

It defines a node structure
"""


class Node:
    """
    This class defines a singly linked list structure
    """
    def __init__(self, data=0, next_node=None):
        """
        Initialize a node structure

        Args:
            data (int): The value of the node
            next_node (Node): The object next node.
        """
        self.data = data
        self.next = next_node

    @property
    def data(self):
        """
        Retrieve the value of the node.

        Args:
            data (int): The value of the node

        Returns:
            The data value
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
        Set properly the value of the data variable

        Args:
            value: The value to set
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Retrieve the object next (Node structure).

        Args:
            next_node (Node): The next node

        Returns:
            Object of a node
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """
        Set properly the value of the data variable

        Args:
            value: The value to set
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


"""
Class: SinglyLinkedList

Singly linked list is a data structure that has one unique direction
which is next. Each "Node" of the Singly list is in the form of a value
and a Node to the next object.
"""


class SinglyLinkedList:
    """
    This class defines a singly linked list

    Attributes:
        head: The first node in the linked list.
    """
    def __init__(self):
        """
        Initialize an empty singly list structure

        Args:
            head (Node): private instance attribute
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position
        in the list (ascending order).

        Args:
            value (int): The value to be inserted.
        """
        new_node = Node(value)

        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.
        """
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return ('\n'.join(nodes))
