#!/usr/bin/env python3

if __name__ == "__main__":
    
    max_value = 4000000 # 4 million
    
    isEven = lambda x: x%2 == 0

    total = 0
    previous = 1
    current = 2
    while current < max_value:
        if isEven(current):
            total += current
        previous, current = current, previous + current
    
    print("Total: {}".format(total))
