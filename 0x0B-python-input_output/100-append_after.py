#!/usr/bin/python3
'''Module to insert text after searching for line containing,
    specific string'''


def append_after(filename="", search_string="", new_string=""):
    '''function that inserts a line of text to a file, after each line,
    containing a specific string.

    Args:
        filename (str, optional): name of file. Defaults to "".
        search_string (str, optional): string to search. Defaults to "".
        new_string (str, optional): string to append. Defaults to "".
    '''
    with open(filename, 'r', encoding="utf-8") as f:
        data = f.readlines()

    with open(filename, 'w', encoding="utf-8") as f:
        string = ""
        for line in data:
            string += line
            if search_string in line:
                string += new_string
        f.write(string)
