#!/usr/bin/python3
'''Function to check object in instance of class and also part of inherited'''


def is_kind_of_class(obj, a_class):
    '''Checking obj instance in class and inheritance
        Args:
            obj:Instance of class or derived class
            a_class: Actual class to check instance in
        Return:
            True or False.
    '''
    if isinstance(obj, a_class):
        return True
    else:
        return False
