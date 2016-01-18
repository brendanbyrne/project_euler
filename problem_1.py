#!/usr/bin/env python3

if __name__ == "__main__":
    
    isGoodNumber = lambda x: x % 3 == 0 or x % 5 == 0

    total = 0
    for i in range(1000):
        if isGoodNumber(i):
            total += i
            
    print("Total is {}".format(total))
