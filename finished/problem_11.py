#!/usr/bin/env python3

import numpy as np
from functools import reduce
from operator import mul

def multiSeq (seq):
    return reduce(mul, seq)

def calcMaxCol (m):
    return max([ multiSeq(col) for col in np.rot90(m)] )

def calcMaxRow (m):
    return max([ multiSeq(row) for row in m ])

if __name__ == "__main__":
    
    with open("problem_11.txt", "r") as f:
        grid = np.array([[int(number) for number in line.strip().split(" ")] for line in f])
    
    max_value = 0

    for row in range(grid.shape[0]-3):
        for col in range(grid.shape[1]-3):
            
            slice = grid[row:row+4, col:col+4]

            values = [ multiSeq(slice.diagonal()),
                       multiSeq(np.flipud(slice).diagonal()) ]
            
            if col%4 == 0:
                values.append(calcMaxCol(slice))
            
            if row%4 == 0:
                values.append(calcMaxRow(slice))
            
            value = max(values)
            
            if value > max_value: max_value = value

    print("max value: {}".format(max_value))

            
            
            
