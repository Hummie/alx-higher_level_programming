#!/usr/bin/python3
'''A class square that inherits from Rectangle'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A class Square'''
    def __init__(self, size):
        '''Initialisation of square'''
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))
