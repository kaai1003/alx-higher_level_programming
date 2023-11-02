#!/usr/bin/python3
if __name__ == "__main__":
    import sys

n = len(sys.argv) - 1
if n == 0:
    print("0 arguments.")
elif n == 1:
    print("1 argument:")
else:
    print("{0:d} arguments:".format(n))
for ar in range(1, (n + 1)):
    print("{0:d}: {1}".format(ar, sys.argv[ar]))
