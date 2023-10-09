#!/usr/bin/python3
'''A class rectangle that inherits from BaseGeometry'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''A class that inherits another'''
    def __init__(self, width, height):
        '''Initialisation'''
        self.integer_validator("height", height)
        self.integer_validator("width", width)

        self.__width = width
        self.__height = height
