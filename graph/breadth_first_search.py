from collections import deque


def breadth_first_Search(adjacency_list, vertex):
    visited = set()

    # add first vertex to visited
    visited.add(vertex)
    queue = deque()
    queue.append(vertex)

    while queue:
        current_vertex = queue.popleft()
        print(current_vertex)

        for edge in adjacency_list[current_vertex]:
            if edge not in visited:
                visited.add(edge)
                queue.append(edge)


adjacency_list = {
    'A':  ['B', 'C'],
    'B':  ['A', 'E'],
    'C':  ['A', 'D'],
    'D':  ['A', 'C', 'E'],
    'E':  ['B', 'D']
}

vertex = "A"
breadth_first_Search(adjacency_list, vertex)
