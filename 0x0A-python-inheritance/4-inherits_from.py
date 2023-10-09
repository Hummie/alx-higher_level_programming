#!/usr/bin/python3
'''Function to check if obj is instance of derived class'''


def inherits_from(obj, a_class):
    '''Checks if instance has been inherited directly or indirectly
        Args:
            obj: Object to check for in classes and subclasses.
            a_class: Baseclass that other classes derive from.
        Return:
            True or False
    '''
    return isinstance(obj, a_class) and obj.__class__ != a_class
