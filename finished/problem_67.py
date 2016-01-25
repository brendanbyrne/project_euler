#!/usr/bin/python3.5

import problem_18 as p18

if __name__ == "__main__":
    triangle = p18.loadTriangle("problem_67.txt")
    
    distance, predecessor = p18.BellmanFord(triangle, "start")

    path, total = p18.buildPath(triangle, distance, predecessor)
    
    print(" + ".join([str(n) for n in path]), " = ", total)
