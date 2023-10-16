#!/usr/bin/python3
'''Class that defines a square'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Class square that inherits from rectangle'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initialization of the class square
        Args:
            size (int):width and height of square.
            x (int):x
            y (int):y
            id (int):Instances of the square.
        '''
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Prints square"""
        return ("[Square] ({}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y, self.size))
