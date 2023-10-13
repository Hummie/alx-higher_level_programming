#!/usr/bin/python3
'''Base module that all functions inherit from''' 


class Base:
    '''A class with a private attribute'''
    __nb_objects = 0


    def __init__(self, id=None):
        '''Initialization of the class'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
