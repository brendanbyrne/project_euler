#!/usr/bin/env python3

def collatz_length (n, cache):
    if n == 1: return 1    
    elif n in cache: return cache[n]
    elif n % 2 == 0: cache[n] = 1 + collatz_length(n // 2, cache)
    else: cache[n] = 1 + collatz_length(3*n +1, cache)
    return cache[n]
    

if __name__ == "__main__":

    cache = {}

    max_start = 0
    max_length = 0
    for n in range(1,1000000):
        length = collatz_length(n, cache)
        
        if length > max_length:
            max_length = length
            max_start = n
            
    print("value: {}, length: {}".format(max_start, max_length))
    
