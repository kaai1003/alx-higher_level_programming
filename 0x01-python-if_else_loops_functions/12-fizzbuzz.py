#!/usr/bin/python3
def fizzbuzz():
    """ prints the numbers from 1 to 100.

    For multiples of 3 print Fizz.
    for multiples of 5 print Buzz.
    For numbers which are multiples of both 3 and 5 print FizzBuzz.
    """
    for n in range(1, 101):
        if n % 5 == 0 and n % 3 == 0:
            print("FizzBuzz ", end="")
        elif n % 5 == 0:
            print("Fizz ", end="")
        elif n % 3 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(n), end="")
