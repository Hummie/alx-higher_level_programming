#!/usr/bin/python3
'''Defining a square with an instance'''


class Square:
    '''Represents a square'''
    def __init__(self, size):
        '''initializing of class square.

           Args:
                size (int): Size of square.
        '''
        self.__size = size
