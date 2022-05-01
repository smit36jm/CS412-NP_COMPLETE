"""
    name:  James Smith

"""

from random import randint, random


def main():
    num_verticies = randint(1, 10)
    graph = {}
   
    for vertex in range(num_verticies):
        num_edges = randint(1, 10)
        graph[vertex] = set()
        for _ in range(num_edges):
            edge = randint(0, num_verticies - 1)
            if edge != vertex:
                graph[vertex].add(str(edge))
    print("graph", graph)
    print(len(graph))
    for v in range(len(graph)):
        edges = graph[v]
        temp = " ".join(edges)
        print(v, temp)

if __name__ == "__main__":
    main()
