#!/usr/bin/python3
'''Defines a square with setter'''


class Square:
    '''Represent the square'''

    def __init__(self, size=0):
        '''Initializes the square

            Args:
                size (int): Size of the square
        '''
        self.size = size

    @property
    def size(self):
        '''Retrieve size of square'''
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Computes area of square'''
        return(self.__size * self.__size)
