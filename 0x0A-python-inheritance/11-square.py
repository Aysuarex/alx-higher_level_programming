#!/usr/bin/python3
""" module square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """ init rectangle """
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        """ str version  """
        return "[Square] {}/{}".format(self.__size, self.__size)
