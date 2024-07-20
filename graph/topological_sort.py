from collections import deque


def topological_sort_util(graph, vertex, visited, stack: deque):
    visited.append(vertex)
    for edge in graph[vertex]:
        if edge not in visited:
            topological_sort_util(graph, edge, visited, stack)

    stack.insert(0, vertex)


def topological_sort(graph):
    visited = []
    stack = []

    for vertex in graph.keys():
        if vertex not in visited:
            topological_sort_util(graph, vertex, visited, stack)

    print(stack)


class Graph:
    def __init__(self, gdict={}):
        self.adjacency_list = gdict

    def add_edge(self, vertex1, vertex2):
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def __str__(self):
        for key, value in self.adjacency_list.items():
            print(key, " : ", value)
        return ""


graph = Graph()
graph.add_vertex('Exercise')
graph.add_vertex('Bath')
graph.add_vertex('Breakfast')
graph.add_vertex('Work')
graph.add_vertex('BuyGrocery')
graph.add_vertex('PrepareBreakfast')
graph.add_vertex('WashDishes')

graph.add_edge("Exercise", "Bath")
graph.add_edge("Bath", "Breakfast")
graph.add_edge("Breakfast", "Work")

graph.add_edge("BuyGrocery", "PrepareBreakfast")
graph.add_edge("PrepareBreakfast", "Breakfast")
graph.add_edge("PrepareBreakfast", "WashDishes")

print(graph)


topological_sort(graph.adjacency_list)
