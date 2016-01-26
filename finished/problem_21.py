#!/usr/bin/env python3

import problem_12 as p12

if __name__ == "__main__":
    
    limit = 10**4

    attempted = []
    pairs = []
    for number in range(1,limit):

        if number in attempted: continue
        
        proper = p12.divisorsOf(number)[:-1]
        potential = sum(proper)
        
        attempted.append(number)
        attempted.append(potential)

        if number == potential: continue 
        
        if sum(p12.divisorsOf(potential)[:-1]) == number:
            pairs.append((number, potential))

    print("Sum of all pairs: ", sum([a+b for a,b in pairs]))
