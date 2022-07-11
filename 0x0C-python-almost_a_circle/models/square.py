#!/usr/bin/python3
"""
module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """ check inputs """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ check inputs """
        return super().width

    @size.setter
    def size(self, value):
        """ check inputs """
        Rectangle.width.fset(self, value)
        Rectangle.height.fset(self, value)

    def update(self, *args, **kwargs):
        """ check inputs """
        if kwargs and (args is None or len(args) == 0):
            if 'size' in kwargs.keys():
                aux = {'width': kwargs['size'], 'height': kwargs['size']}
                kwargs.update(aux)
            super().update(*args, **kwargs)
        else:
            args_list = list(args)
            if len(args) > 1:
                args_list.insert(1, args[1])
            super().update(*args_list, **kwargs)

    def to_dictionary(self):
        """ check inputs """
        new_dict = {'id': self.id,
                    'size': self.height,
                    'x': self.x,
                    'y': self.y}
        return new_dict
