#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_count = len(sys.argv)
    if args_count-1 == 1:
        print("{:d} argument".format(args_count - 1), end="")
    else:
        print("{:d} arguments".format(args_count - 1), end="")
    if args_count - 1 == 0:
        print(".")
    else:
        print(":")
    for x in range(1, args_count):
        print("{:d}: {:s}".format(x, sys.argv[x]))
