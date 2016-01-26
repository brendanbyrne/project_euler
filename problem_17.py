#!/usr/bin/env python3

ones =  [None, "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens =  [None, None, "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def thousands (s):
    string = ""
    
    if len(s) != 4: pass
    else:
        digit = ones[int(s[0])]
        if digit is None: pass
        else:
            return string = digit + "thousand"
    return string

def hundreds (s):
    string = ""
    
    if len(s) != 3: pass
    else:
        digit = ones[int(s[0])]
        if digit is None:
            next = int(s[1:])
            if next == 0: pass
            else: string = "and"
        else:
            base = digit + "hundred"
            next = int(s[1:])
            if next == 0: string =  base + "hundred"
            else: string = base + "hundred" + "and"
    return string

def tens (s):
    string = ""
    
    if len(s) != 2: pass
    else:
        number = int(s)
        if 10 <= number and number <= 19:
            number
        

def numberToWord (number):

    string = str(number)
    

    
            
            

if __name__ == "__main__":
    
    print(sum([len(numberToWord(number)) for number in range(1,1001)]))
