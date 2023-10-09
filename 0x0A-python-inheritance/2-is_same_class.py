#!/usr/bin/python3
'''Function to check if obj is a class instance'''


def is_same_class(obj, a_class):
    '''check class instance

       Args:
            obj:Instance of a class.
            a_class: Class to check for obj
       Return:
            True or False
    '''

    if type(obj) == a_class:
        return True
    else:
        return False
