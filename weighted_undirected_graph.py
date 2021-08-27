from random import randint

from undirected_graph import UndirectedGraph
from undirected_graph_edge import UndirectedGraphEdge


class WeightedUndirectedGraph(UndirectedGraph):
    def __init__(self):
        super().__init__()

    def initialize(self, rand=1):
        if rand == 1:
            for i in range(0, self.n):
                for j in range(i + 1, self.n):
                    if randint(1, 10) <= 6:
                        self.adjacency_matrix[i, j] = 1
                        self.adjacency_matrix[j, i] = 1
                        self.edges.append(UndirectedGraphEdge(self.vertices[i], self.vertices[j], randint(1, 100)))
        else:
            for i in range(0, self.n):
                for j in range(i + 1, self.n):
                    if (i + j) % 2 == 1:
                        self.adjacency_matrix[i, j] = 1
                        self.adjacency_matrix[j, i] = 1
                        self.edges.append(UndirectedGraphEdge(self.vertices[i], self.vertices[j], randint(1, 100)))
