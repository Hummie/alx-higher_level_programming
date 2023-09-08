#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    res = 0

    for args in sys.argv[1:]:
        argt = int(args)
        res += argt
    print("{}".format(res))
