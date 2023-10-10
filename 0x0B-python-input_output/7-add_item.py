#!/usr/bin/python3
'''Module that loads, adds args and save to file'''
from sys import argv


load_file = __import__('6-load_from_json_file').load_from_json_file
save_file = __import__('5-save_to_json_file').save_to_json_file


try:
    item_list = load_file('add_item.json')
except (ValueError, FileNotFoundError):
    item_list =[]

for item in argv[1:]:
    item_list.extend(item)

save_file(item_list, 'add_item.json')
    
