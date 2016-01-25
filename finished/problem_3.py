#! /usr/bin/env python3

if __name__ == "__main__":
    
    n = 600851475143
    
    i = 2
    factors = {}
    while i * i < n:
        if n % i:
            i += 1
        else:
            factors[i] = factors.get(i, 0) + 1
            n //= i
    
    for f in sorted(factors.keys()):
        print(f, factors[f])
    
    print("Largest prime factor: {}".format(n))
    
        
    check = [n % i == 0 for i in range(2, n)]
    print(not any(check))
