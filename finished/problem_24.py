#!/usr/bin/env python3

from itertools import permutations as nPr

if __name__ == "__main__":

    string = "0123456789"
    
    for i, combination in enumerate(nPr(string)):
        if i == 999999:
            print("".join(combination))
            break
