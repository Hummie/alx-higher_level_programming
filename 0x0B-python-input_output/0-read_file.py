#!/usr/bin/python3
'''A function that reads and prints a text file'''


def read_file(filename=""):
    with open(filename, mode='r', encoding="utf-8") as file_read:
        print(file_read.read(), end="")
