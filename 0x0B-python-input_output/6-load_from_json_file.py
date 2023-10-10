#!/usr/bin/python3
'''Module to create an obj from json file'''
import json


def load_from_json_file(filename):
    '''Create obj from json file
        Args:
            filename:Name of file.
        Return:
            python obj.
    '''
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
