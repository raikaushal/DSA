from collections import deque


def depth_first_Search(adjacency_list, vertex):
    visited = set()

    # add first vertex to visited
    visited.add(vertex)
    stack = deque()
    stack.append(vertex)

    while stack:
        current_vertex = stack.pop()
        if current_vertex not in visited:
            print(current_vertex)
            visited.add(current_vertex)

        for edge in adjacency_list[current_vertex]:
            if edge not in visited:
                stack.append(edge)


adjacency_list = {
    'A':  ['B', 'C'],
    'B':  ['A', 'E'],
    'C':  ['A', 'D'],
    'D':  ['A', 'C', 'E'],
    'E':  ['B', 'D']
}

vertex = "A"
depth_first_Search(adjacency_list, vertex)
