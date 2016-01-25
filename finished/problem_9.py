#!/usr/bin/env python3

if __name__ == "__main__":
    
    test = []

    for a in range(1, 998 + 1):
        for b in range(1, 998 + 1):
            c = 1000 - a - b
            
            if c <= 0: continue
            
            if a**2 + b**2 == c**2:
                print(a*b*c)
                break
        break # avoids symetry
        
