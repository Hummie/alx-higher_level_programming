#!/usr/bin/python3
'''A function that reads and prints a text file'''


def read_file(filename=""):
    '''Reading file and printing to stdout
        Args:
            filename: name of file
    '''
    with open(filename, 'r', encoding="utf-8") as file_read:
        print(file_read.read(), end='')
