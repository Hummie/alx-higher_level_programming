#!/usr/bin/python3
def safe_print_integer(value):
    while True:
        try:
            if isinstance(value, int):
                print("{:d}".format(value))
                return True
            else:
                return False
        except Exception:
            print()
