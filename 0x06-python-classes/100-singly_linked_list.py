#!/usr/bin/python3
""" singly linked list"""


class Node:
    """ class node """
    def __init__(self, data, next_node=None):
        """ init node
        Args:
            data (int):data to store.
            next_node : address next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None
        self.linked_list = []

    def sorted_insert(self, value):
        new_node = Node(value)
        new_node.next_node = self.__head
        self.__head = new_node
        self.linked_list = []
        aux = Node(self.__head.data, self.__head.next_node)
        while aux is not None:
            self.linked_list.append(aux.data)
            aux = aux.next_node
        self.linked_list.sort()

    def __str__(self):
        return '\n'.join(list(map(str, self.linked_list)))
