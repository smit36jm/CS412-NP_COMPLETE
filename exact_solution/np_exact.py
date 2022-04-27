"""
    name:  Alyssa Sharp
    
"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
import itertools


def np_checker(graph, colors):
    for u in graph:
        for v in graph[u]:
            if colors[u] == colors[v]:
                return False
    return True

def main():
    num_verticies = int(input())
    edges = {}
    for _ in range(num_verticies):
        edge_list = [int(x) for x in input().split()]
        i = edge_list[0]
        edges[i] = []
        for edge in edge_list[1:]:
            edges[i].append(edge)

    # outlier = verticies aren't connected || just one vertex == 1 color
    # outlier = num verticies = 0 == 0 colors

    # want to pass itertools a product [1, 2], repeat = num_verticies
    # then                     product [1, 2, 3], repeat = num_verticies
    # then                     product [1, 2, 3, ... num_verticies (-1??), repeat = num_verticies
    # if we ever recieve true, stop it because that's our min (planning on starting from 2 and working up)
    
    min_found = False

    while min_found == False:
        num_colors = 2
        for colors in itertools.product(range(1, num_colors + 1), repeat=num_verticies):
            if np_checker(edges, colors) == True:
                min_found = True
                print(num_colors)
                break    
        num_colors += 1

if __name__ == "__main__":
    main()
