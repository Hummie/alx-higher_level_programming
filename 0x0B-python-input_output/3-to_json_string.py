#!/usr/bin/python3
'''Module that returns JSON rep of obj string'''
import json


def to_json_string(my_obj):
    '''Returns json rep of a string
        Args:
            my_obj: Object to be returned as json
        Return:
            json string
    '''
    return json.dumps(my_obj)
