#!/usr/bin/python3
'''Class defining a rectangle'''


class Rectangle:
    '''A class rectangle'''

    def __init__(self, width=0, height=0):
        '''Initialisation of the rectangle
        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Retrieving and setting width'''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Retrieving and setting height.'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Returns area of rectangle'''
        return (self.__width * self.__height)

    def perimeter(self):
        '''Returns perimeter of rectangle'''
        if self.__height == 0 or self.width == 0:
            return 0
        return (self.__height + self.width) * 2

    def __str__(self):
        '''Returns a printable string representation of rectangle'''
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
