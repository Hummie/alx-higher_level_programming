#!/usr/bin/python3
'''Module that converts json str to python obj'''
import json


def from_json_string(my_str):
    '''Returns a python obj from json str
        Args:
            my_str:String to be converted or deserialized.
        Return:
            python obj.
    '''
    return json.loads(my_str)
