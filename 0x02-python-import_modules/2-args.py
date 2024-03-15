#!/usr/bin/python3
import sys

def main(*argv):
    x = 0
    args_count = len(sys.argv) - 1
    if args_count == 1:
        print("{:d} argument:".format(1))
    elif args_count == 0:
        print("{:d} arguments.".format(1))
    else:
        print("{:d} arguments:".format(1))
    for args in sys.argv:
        if (x != 0):
            print("{}: {}".format(x, args))
        x += 1

if __name__ == "__main__":
    main()
