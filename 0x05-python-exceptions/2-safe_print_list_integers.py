#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = print_int = 0
    while True:
        try:
            if index < x:
                print("{:d}".format(my_list[index]), end='')
                index += 1
                print_int += 1
            else:
                print()
                return print_int
        except (TypeError, ValueError):
            index += 1
