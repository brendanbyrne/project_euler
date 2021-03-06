#!/usr/bin/env python3

if __name__ == "__main__":
    with open("problem_13.txt", "r") as f:
        data = [number.strip() for number in f]
    
    total = 0
    for string in data:
        total += int(string)

    print(str(total)[:10])


    import sys
    sys.exit()

    # old attempts at carry addition, might need to revisit
    
    foo = 0
    for d in data1:
        foo += d
        while foo > 10**10:
            foo -= 10**10
    print("foo ", foo)
    

    number = []
    
    base = 10    
    carry = 0

    for digits in zip(*data):
        total = sum(map(int, digits)) + carry
        carry = total // base
        number.append(total % base)
        
    while carry > base:
        number.append(carry % base)
        carry //= base
        
    if carry != 0:
        number.append(carry)
    
    number.reverse()
    #print("".join([str(d) for d in number]))

    total = 0
    for n in data:
        total += int(n[-10:])
    print("total ", total)
