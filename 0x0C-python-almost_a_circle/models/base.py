#!/usr/bin/python3
'''Base module that all functions inherit from''' 
import json


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

    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): list of dictionaries.

        Returns:
            str: jason string representation.
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)
