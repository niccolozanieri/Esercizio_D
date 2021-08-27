import numpy as np
from random import randint

from undirected_graph_vertex import UndirectedGraphVertex
from undirected_graph_edge import UndirectedGraphEdge


class UndirectedGraph:
    def __init__(self, n=0):
        self.adjacency_matrix = np.zeros((n, n), dtype=np.int16)
        self.n = n
        self.vertices = []
        self.edges = []

        for i in range(0, n):
            self.vertices.append(UndirectedGraphVertex(i))

    def initialize(self, rand=1):
        if rand == 1:
            for i in range(0, self.n):
                for j in range(i + 1, self.n):
                    if randint(1, 10) <= 6:
                        self.adjacency_matrix[i, j] = 1
                        self.adjacency_matrix[j, i] = 1
                        self.edges.append(UndirectedGraphEdge(self.vertices[i], self.vertices[j]))
        else:
            for i in range(0, self.n):
                for j in range(i + 1, self.n):
                    if (i + j) % 2 == 1:
                        self.adjacency_matrix[i, j] = 1
                        self.adjacency_matrix[j, i] = 1
                        self.edges.append(UndirectedGraphEdge(self.vertices[i], self.vertices[j]))

    def to_string(self):
        for i in range(0, self.n):
            for j in range(0, self.n):
                print(self.adjacency_matrix[i, j], end=' ')
            print('\n', end='')

    def find_edge(self, edge):
        for item in self.edges:
            if item.is_equal(edge):
                return True

        return False
