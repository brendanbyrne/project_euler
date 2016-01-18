#!/usr/bin/env python3

if __name__ == "__main__":
    sosq = sum([i**2 for i in range(1,101)])
    sqos = sum(range(1,101))**2
    
    print(sqos - sosq)
