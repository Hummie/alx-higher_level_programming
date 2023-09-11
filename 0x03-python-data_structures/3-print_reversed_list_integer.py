#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        list_reverse = list(reversed(my_list))
        for members in list_reverse:
            print("{:d}".format(members))
