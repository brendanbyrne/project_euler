#!/usr/bin/env python3

if __name__ == "__main__":
    
    isValid= lambda x: all([x%i == 0 for i in range(1,21)])
    
    n = 9699690 # multiple of primes
    step = 9699690 # minimum step size
    while not isValid(n):
        n += step
    print(n)
    
