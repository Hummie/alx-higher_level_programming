#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        sys.exit(1)

    res = 0

    for args in sys.argv[1:]:
        argt = int(args)
        res += argt
    print("{}".format(res))
