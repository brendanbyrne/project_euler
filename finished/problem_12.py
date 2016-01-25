#!/usr/bin/env python3

def divisorsOf (number):
    up = 1
    divisors = set([up])
    
    down = number
    
    while up < down:
        if number % up == 0:
            divisors.add(up)
            down = number // up
            divisors.add(down)
            
        up += 1
        
    return sorted(list(divisors))
    
if __name__ == "__main__":
    
    min_divisors = 500

    triangle = 1
    base = 1
    
    while len(divisorsOf(triangle)) < min_divisors:
        base += 1
        triangle += base
    print(triangle)
