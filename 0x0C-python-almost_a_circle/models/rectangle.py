#!/usr/bin/python3
'''A class rectangle that inherits from class base'''
from models.base import Base


class Rectangle(Base):
    '''Class rectangle that defines properties of a rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialization of the class rectangle
        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): x.
            y (int): y
            id (int): Identify instances of class rectangle.
        '''
        self.__width = width
        self.__height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            '''Retrieves the width
            Returns:
                int:Width of rectangle
            '''
            return self.__width

        @width.setter
        def width(self, value):
            '''Sets the width of the rectangle
            Args:
                Value (int):Width of the rectangle
            '''
            self.__width = value

        @property
        def height(self):
            '''Retrieves the height
            Returns:
                int:Height of rectangle
            '''
            return self.__height

        @height.setter
        def height(self, value):
            '''Sets the height of the rectangle
            Args:
                value (int):Height of the rectangle
            '''
            self.__height = value

        @property
        def x(self):
            '''Gets the value of x
            Returns:
                int:Value of x
            '''
            self.__x

        @x.setter
        def x(self, value):
            '''Sets the value of x
            Args:
                Value (int):x
            '''
            self.__x

        @property
        def y(self):
            '''Gets y
            Returns:
                int:Value of y
            '''
            self.__y

        @y.setter
        def y(self, value):
            ''' Sets the value of y
            Args:
                value (int):y
            '''
            self.__y
