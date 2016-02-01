#!/usr/bin/env python3

from problem_4 import isPalindrome as pal

if __name__ == "__main__":
    
    numbers = [n for n in range(1, 10**6) if pal(n) and pal(bin(n)[2:])]
    
    print(sum(numbers))
