'''
Author: Rhea Morris 
Date: 04/29/2022

Time Complexity: O(n^2) in the worst case, but usually takes linear time.

Approach: This approximation algorithm takes a greedy approach by picking the node
with the highest degree and coloring it. Then, it removes the node from the graph and its edges.
Then, it repeats the process until there are no more nodes to be colored, or if there are isolated nodes
left then it colors them all with the same color.

Citation: https://www.cs.cmu.edu/~avrim/Papers/coloring_worstcase.pdf
          Used this to read about different ways of approximating the min graph coloring problem.
          Wrote my own solution.
'''
def main(): 
    num_vertices = int(input())
    graph = {}
    degree = {}
    for i in range(num_vertices):
        list = [int (x) for x in input().split()]
        graph[list[0]] = list[1:]
        degree[list[0]] = len(list[1:])
    print(min_graph_coloring_2(graph, degree))

def min_graph_coloring_2(graph, degree, num=1):
    max = 0
    max_vertex = degree.get(max)
    for vertex in degree:
        if degree[vertex] > max:
            max = degree[vertex]
            max_vertex = vertex
    #when there is only 1 isolated node color it and return
    if max == 0:
        return num
    graph.pop(max_vertex)
    degree.pop(max_vertex)
    #remove all the edges conected to the max vertex
    for node in graph:
        for neighbor in graph[node]:
            if neighbor == max_vertex:
                graph[node].remove(neighbor)
                degree[node] -= 1
    return min_graph_coloring_2(graph, degree, num+1)
               
if __name__ == "__main__":
    main()
