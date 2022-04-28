def main():
    num_vertices = int(input())
    dict = {}
    degree = {}
    for i in range(num_vertices):
        list = [int (x) for x in input().split()]
        dict[list[0]] = list[1:]
        degree[list[0]] = len(list[1:])
    print("Approximation = ",min_graph_coloring_2(dict, degree))

def min_graph_coloring_2(dict, degree, num=0):
    if len(dict) == 0:
        return num
    #print(dict)
    #print(degree)
    max = 0
    max_vertex = degree.get(max)
    for vertex in degree:
        if degree[vertex] > max:
            max = degree[vertex]
            max_vertex = vertex
    if max_vertex == None:
        return num + 1
    #print("max vertex", max_vertex)
    num += 1
    visited = []
    visited.append(max_vertex)
    dict.pop(max_vertex)
    degree.pop(max_vertex)
    for node in dict:
        for neighbor in dict[node]:
            if neighbor == max_vertex:
                dict[node].remove(neighbor)
                degree[node] -= 1
   #print("num",num)
    num = min_graph_coloring_2(dict, degree, num)
    return num
    
            
if __name__ == "__main__":
    main()
