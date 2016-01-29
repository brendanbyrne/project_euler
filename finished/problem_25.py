#!/usr/bin/env python3

if __name__ == "__main__":
    
    first  = 1
    second = 1

    count = 2
    while len(str(second)) < 1000:
        first, second = second, first+second
        count += 1
    print(count)
