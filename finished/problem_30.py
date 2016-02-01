#!/usr/bin/env python3

if __name__ == "__main__":

    test = lambda x: x == sum([int(digit)**5 for digit in str(x)])

    test_range = range(2, 1000000)

    number = [number for number in test_range if test(number)]
    
    print(sum(number))
