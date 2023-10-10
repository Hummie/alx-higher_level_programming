#!/usr/bin/python3
'''A function that reads and prints a text file'''


def read_file(filename=""):
    with open(filename, mode='r', encoding="utf-8") as file_read:
        read_data = file_read.read()
        print(read_data, end="")
