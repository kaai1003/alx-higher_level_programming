#!/usr/bin/python3
if __name__ == "__main__":
    import sys
n = len(sys.argv)
if n == 1:
    print("{0:d} arguments.".format(n - 1))
elif n == 2:
    print("{0:d} argument:".format(n - 1))
else:
    print("{0:d} arguments:".format(n - 1))
