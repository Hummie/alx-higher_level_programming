#!/usr/bin/python3
'''Module that writes to a file using json'''
import json


def save_to_json_file(my_obj, filename):
    '''Writes to a file
        Args:
            my_obj:Object to be written to file.
            filename:Name of file.
    '''
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
