"""
    name:  Alyssa Sharp

"""

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

    if num_verticies == 0:
        print(0)
    else:
        min_found = False

        num_colors = 1
        while min_found == False or num_colors == num_verticies:
            for color_list in itertools.product(range(1, num_colors + 1), repeat=num_verticies):
                colors = {}
                i = 0
                for u in edges:
                    colors[u] = color_list[i]
                    i += 1
                # print(color_list)
                if np_checker(edges, colors) == True:
                    min_found = True
                    # print(colors)
                    print(num_colors)
                    break    
            num_colors += 1

if __name__ == "__main__":
    main()
