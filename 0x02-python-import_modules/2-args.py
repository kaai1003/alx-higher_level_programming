#!/usr/bin/python3
if __name__ == "__main__":
    import sys

n = len(sys.argv)
if n == 1:
    print("{0:d} arguments.".format(n - 1))
elif n == 2:
    print("{0:d} argument :".format(n - 1))
    for ar in range(1, n):
        print("{0:d}: {1}".format(ar, sys.argv[ar]))
else:
    print("{0:d} arguments.".format(n - 1))
    for ar in range(1, n):
        print("{0:d}: {1}".format(ar, sys.argv[ar]))
