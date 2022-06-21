#!/usr/bin/python3
""" class Square that defines a square"""


class Square:
    """ class Square that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """ init square

        Args:
            value (int): size of the square.
            position (tuple): position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """int: private size.

        Returns:
            Private size.
        """
        return self.__size

    @property
    def position(self):
        """tuple position"""

        return self.__position

    @position.setter
    def position(self, value):
        """ set posotion of the square

        Args:
            value (tuple): position
        """
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(value) is not 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value  #: position of the square

    @size.setter
    def size(self, value):
        """Sets value into size, must be int.

        Args:
            value (int): size of the square.
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value  #: size of the square

    def area(self):
        """returns the area

        Returns:
            area.
        """
        return self.__size**2

    def my_print(self):
        """prints in stdout the square with the character #"""

        if self.__size != 0:
            for k in range(self.__position[1]):
                print()
            for i in range(self.__size):
                if (self.__position[0] != 0):
                    for l in range(self.__position[0]):
                        print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()

    def __str__(self):
        str_square = []

        if self.__size != 0:
            for k in range(self.__position[1]):
                str_square.append('\n')
            for i in range(self.__size):
                if (self.__position[0] != 0):
                    for l in range(self.__position[0]):
                        str_square.append(' ')
                for j in range(self.__size):
                    str_square.append('#')
                if (i < self.__size - 1):
                    str_square.append('\n')
        return ''.join(str_square)
