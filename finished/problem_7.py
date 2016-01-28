#!/usr/bin/env python3
from math import floor, sqrt
import sys

def squareMultipleOffset (number, max_value):
    square = number**2
    offset = square
    
    while offset <= max_value:
        yield offset        
        offset += number

def firstNPrimes (size_primes):
    max_size = size_primes**2
    first_prime = 2
    
    sieve = [True for _ in range(first_prime, max_size + 1)]
    primes = []
    
    
    potential_prime = first_prime
    while len(primes) < size_primes:
        if sieve[potential_prime - first_prime]:
            primes.append(potential_prime)
            
            for multiple in squareMultipleOffset(potential_prime, max_size):
                sieve[multiple - first_prime] = False
                                
        potential_prime += 1
    
    return primes
        
def basicSieve (min_value, max_value, *, initial_primes = []):
    
    sieve = [True for _ in range(min_value, max_value+1)]
    
    for prime in initial_primes:
        for index, has_potential in enumerate(sieve):
            value = index + min_value
            if has_potential and value%prime == 0:
                sieve[index] = False                

    for base_value in range(min_value, floor(sqrt(max_value))):
        
        base_index = base_value - min_value
        if sieve[base_index]:

            for new_value in squareMultipleOffset(base_value, max_value):
                new_index = new_value - min_value
                sieve[new_index] = False
    
    return [index + min_value for index, is_prime in enumerate(sieve) if is_prime]
    
    
if __name__ == "__main__":
    
    primes = []
    min_value = 2      # necessary
    max_value = 100000 # pulled something out of thin air
    
    while len(primes) < 10001:
        primes.extend(basicSieve(min_value, max_value, initial_primes = primes))
        
        print("Primes length: {}".format(len(primes)))
        
        min_value = max_value + 1
        max_value = min_value + 10000 # same here, no real rhyme or reason for growth rate
        
    print("10,001st prime: {}".format(primes[10000]))
    
    print("10,001st prime: {}".format(firstNPrimes(10001)[-1]))
                                    
