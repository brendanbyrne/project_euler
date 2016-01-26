#!/usr/bin/env python3

from math import factorial

if __name__ == "__main__":
    print(sum([int(digit) for digit in str(factorial(100))]))
