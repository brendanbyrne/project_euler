#!/usr/bin/env python3

if __name__ == "__main__":

    isPalindrome = lambda num: str(num) == str(num)[::-1]
    
    lb = 100
    ub = 999
    
    palindromes = { i*j: (i, j) for i in range(lb, ub+1) for j in range(i, ub+1) if isPalindrome(i*j) }

    
    value = max(palindromes.keys())
    
    print("{} * {} = {}".format(palindromes[value][0], palindromes[value][1], value))
