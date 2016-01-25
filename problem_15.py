#!/usr/bin/env python3

def makeList (size_row, size_col):
    rows = size_row + 1
    cols = size_col + 1
    
    number_of_nodes = rows*cols
    
    edges = [set() for _ in range(number_of_nodes)]
    
    for r in range(rows):
        for c in range(cols):

            node_index = (cols*r + c)
                
            if c < cols-1:
                right_node = node_index + 1
                
                edges[node_index].add(right_node)
                
            if r < rows-1:
                below_node = node_index + cols

                edges[node_index].add(below_node)

    return {n: e for n, e in enumerate(edges)}

def DFS (graph, visited, end, paths):
    back = visited[-1]
    
    for node in graph[back]:
        
        if node in visited: continue
        
        if node == end:
            visited.append(node)
            path.append(visisted)
            # http://www.technical-recipes.com/2011/a-recursive-algorithm-to-find-all-paths-between-two-given-nodes/
    

def findAllPaths (graph, start, end):
    
    paths = []
    DFS(graph, [start], end, paths)
    
    return paths

if __name__ == "__main__":
    
    # 0 -> 1 -> 2

    # |    |    |
    # v    v    v

    # 3 -> 4 -> 5

    # |    |    |
    # v    v    v

    # 6 -> 7 -> 8
    
    graph = makeList(20, 20)
    
    
    print( len( findAllPaths(graph, 0, 19) ) )

    
    
