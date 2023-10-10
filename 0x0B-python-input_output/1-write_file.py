#!/usr/bin/python3
'''A function that writes string to a textfile and returns num of char'''


def write_file(filename="", text=""):
    '''Writes to file and returns number of charachters
        Args:
            filename: Name of file.
            text: Text to be inputed.
        Return:
            Number of charachters
    '''
    with open(filename, 'w', encoding="utf-8") as f:
        char_written = f.write(text)
        return char_written
