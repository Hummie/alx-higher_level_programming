#!/usr/bin/python3
def safe_print_division(a, b):
    while True:
        try:
            value = a / b
            print("Inside result: {:.1f}".format(value))
        except ZeroDivisionError:
            value = None
            print("Inside result: {}".format(value))
        finally:
            return value
