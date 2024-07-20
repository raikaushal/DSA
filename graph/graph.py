
class Graph:
    def __init__(self, gdict={}):
        self.adjacency_list = gdict

    def add_edge(self, vertex1, vertex2):
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        self.adjacency_list[vertex1].remove(vertex2)
        self.adjacency_list[vertex2].remove(vertex1)

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def remove_vetex(self, vertex):
        del self.adjacency_list[vertex]
        for key in self.adjacency_list.keys():
            if vertex in self.adjacency_list[key]:
                self.adjacency_list[key].remove(vertex)

    def __str__(self):
        for key, value in self.adjacency_list.items():
            print(key, " : ", value)
        return ""


# gdict = {
#     "a": ["b", "c"],
#     "b": ["a", "d", "e"],
#     "c": ["a", "e"],
#     "d": ["b", "e", "f"],
#     "e": ["b", "c", "d"],
#     "f": ["d", "e"]
# }

graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("A", "D")

graph.add_edge("C", "D")

graph.add_edge("B", "E")
graph.add_edge("D", "E")

print(graph)
