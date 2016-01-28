#!/usr/bin/python3.5

from math import inf
from copy import deepcopy
from functools import reduce

from butils.generators import window

def loadTriangle (filename):
    
    with open(filename, "r") as f:
        weights = [-int(s) for s in f.readline().split()]
        
        graph = {"start": [(node, w) for node, w in enumerate(weights)]}
        prev_nodes = range(len(weights))

        for node in prev_nodes: graph[node] = []

        row = len(weights)

        for line in f:
            row += 1
            weights = [-int(s) for s in line.strip().split(" ")]
            nodes = range(prev_nodes[-1] + 1, prev_nodes[-1] + row + 1)
            
            i = 0
            for n, w in zip(nodes, weights):
                if i == 0:
                    graph[n-row+1].append((n, w))
                    pass
                elif i == row-1:
                    graph[n-row].append((n, w))
                else:
                    graph[n-row].append((n, w))
                    graph[n-row+1].append((n,w))
                i += 1

            prev_nodes = nodes
            for node in prev_nodes: graph[node] = []
            
        for n in prev_nodes:
            graph.get(n, []).append(("finish", 0))
        
        graph["finish"] = []
        
        return graph
    
def BellmanFord (graph, start):
    
    distance    = {vertex: inf for vertex in graph.keys()}
    predecessor = {vertex: None for vertex in graph.keys()}
    
    distance[start] = 0
    
    i = 0
    while True:
        print(i)
        i+=1
        prev_distance = deepcopy(distance)
        
        for vertex in graph.keys():
            for node, weight in graph[vertex]:
                if distance[vertex] + weight < distance[node]:
                    distance[node] = distance[vertex] + weight
                    predecessor[node] =  vertex
                    
        if all([distance[k] == prev_distance[k] for k in graph.keys()]):
            break
        
    
    for vertex in graph.keys():
        for node, weight in graph[vertex]:
            if distance[vertex] + weight < distance[node]:
                print("vertex: {}, node: {}, contains negative-weight cycle".format(vertex, node))
                
    return distance, predecessor

def Dijkstra (graph, start, target):
    
    distance    = {vertex: inf for vertex in graph.keys()}
    predecessor = {vertex: None for vertex in graph.keys()}
    Q           = set(graph.keys())
    
    distance[start] = 0

    wMin = lambda u,v: u if distance[u] < distance[v] else v
    
    def wMax (u,v):
        if distance[u] == inf and distance[v] == inf:
            return u
        elif distance[u] != inf and distance[v] != inf:
            return u if distance[u] > distance[v] else v
        else:
            return u if distance[u] != inf else v
            
    u = distance[start]

    while len(Q) != 0:
        print("="*80)
        for v in Q:
            if distance[v] != inf: print("V: {}, Distance: {}".format(v, distance[v] - distance[u]))
        print("Q: {}".format(Q))
        #u = reduce(wMin, Q)
        u = reduce(wMax, Q)
        print("U: {}, Distance: {}".format(u, distance[u]))
        
        if u == target: break
        
        Q.discard(u)

        for v, weight in graph[u]:
            alt = distance[u] + weight
            if alt < distance[v]:
                distance[v] = alt
                predecessor[v] = u
    
    return distance, predecessor


def buildPath (graph, distance, predecessor):
    next_node = predecessor["finish"]
    
    path = []
    while next_node != "start":
        path.append(next_node)
        next_node = predecessor[next_node]
    
    path.append("start")
    
    path.reverse()

    numbers = []
    for u, v in window(path, 2):
        for node, weight in graph[u]:
            if node == v:
                numbers.append(-weight)

    return numbers, -distance["finish"]

def buildDPath (graph, distance, predecessor):

    u = "finish"
    path = [u]
    
    while predecessor[u] != "start":
        u = predecessor[u]
        path.append(u)
    path.append("start")
    
    path.reverse()
    
    numbers = []
    for u, v in window(path, 2):
        for node, weight in graph[u]:
            if node == v:
                numbers.append(-weight)
    
    return numbers, -distance["finish"]

if __name__ == "__main__":

    #           start
    #             3
    #             0
    #         7        4
    #         1        2
    #     2       4        6
    #     3       4        5
    # 8       5        9       3
    # 6       7        8       9
    #             0
    #           finish

    triangle = loadTriangle("problem_18.txt")
    
    distance, predecessor = BellmanFord(triangle, "start")

    path, total = buildPath(triangle, distance, predecessor)

    print(" + ".join([str(n) for n in path]), " = ", total)


    distance, predecessor = Dijkstra(triangle, "start", "finish")

    path, total = buildDPath(triangle, distance, predecessor)

    print(" + ".join([str(n) for n in path]), " = ", total)
