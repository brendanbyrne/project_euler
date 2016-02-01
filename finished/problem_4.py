#!/usr/bin/env python3

def isPalindrome (num): 
    return str(num) == str(num)[::-1]

if __name__ == "__main__":
    
    lb = 100
    ub = 999
    
    palindromes = { i*j: (i, j) for i in range(lb, ub+1) for j in range(i, ub+1) if isPalindrome(i*j) }

    
    value = max(palindromes.keys())
    
    print("{} * {} = {}".format(palindromes[value][0], palindromes[value][1], value))
