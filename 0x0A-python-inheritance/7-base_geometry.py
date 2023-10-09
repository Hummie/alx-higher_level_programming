#!/usr/bin/python3
'''Defines a class BaseGeometry'''


class BaseGeometry:
    '''A class representation'''

    def area(self):
        '''A method area that hasn't been implemented'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''A method that validates parameter value.
            Args:
                Name:A string of characters.
                Value:Value to be validated using exeptions
        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
