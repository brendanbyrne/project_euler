#!/usr/bin/env python3

from string import ascii_uppercase

if __name__ == "__main__":
    alphabet = " " + ascii_uppercase
    
    
    with open("problem_22.txt", "r") as f:
        names = sorted([raw.replace("\"", "") for raw in f.read().strip().split(",")])

    total = 0
    for i, name in enumerate(names):
        total += (i + 1) * sum([alphabet.index(letter) for letter in name])
    
    print(total)
