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

    @property
    def size(self):
        """Property retriever for size.

        Returns:
            int: size of one side of square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """Property setter for width of square.
        Args:
            value (int): width of square.
        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute

        Args:
            *args (tuple): arguments.
            **kwargs (dict): double pointer to a dictionary.
        """
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)
