#!/usr/bin/python3
# 100-singly_linked_list.py - By TM
""" class Node that defines a node of a singly linked list """


class Node:
    """ Instantiation with data and next_node """
    def __init__(self, data, next_node=None):
        """ instance attributes data, next_node """
        self.data = data
        self.next_node = next_node

        """ getter that retrive data """
        @property
        def data(self):
            return self.__data

        """ property setter to set data """
        @data.setter
        def data(self, value):
            """ check if value is an integer """
            if (not isinstance(value, int)):
                raise ValueError("data must be an integer")
            self.__data = value

        """ getter that retrive next_node """
        @property
        def next_node(self):
            return self.__next_node

        """ property setter to set next_node """
        @next_node.setter
        def next_node(self, value):
            """ check if value is Node and is None """
            if (not isinstance(value, Node) or value is not None):
                raise TypeError("next_node must be a Node object")
            self.__next_node = value



class SinglyLinkedList:
    """ Simple instantiation """
    def __init__(self):
        """ Private instance attribute: head (no setter or getter) """
        self.__head = None

    """ Public instance method that adds a new node in a sorted list """
    def sorted_insert(self, value):
        new_node = Node(value)

        if (self.__head is None):
            self.__head = new_node
            return

        if (value < self.__head.data):
            new_node.next_node = self.__head
            self.__head = new_node
            return

        curr = self.__head

        while (curr.next_node is not None and curr.next_node.data < value):
            curr = curr.next_node

        new_node.next_node = curr.next_node
        curr.next_node = new_node

    """ Public instance method that prints the list """
    def __str__(self):
        """ print() representation of a SinglyLinkedList """
        if self.__head is None:
            return ""

        curr = self.__head
        sll = str(curr.data)

        while curr.next_node is not None:
            curr = curr.next_node
            sll += "\n" + str(curr.data)

        return sll
