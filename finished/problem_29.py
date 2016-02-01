#!/usr/bin/env python3

if __name__ == "__main__":
    
    numbers = set([a**b for a in range(2, 101) for b in range(2,101)])
    
    print(len(numbers))
    
