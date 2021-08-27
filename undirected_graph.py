import numpy as np
from random import randint

from undirected_graph_vertex import UndirectedGraphVertex
from undirected_graph_edge import UndirectedGraphEdge


class UndirectedGraph:
    def __init__(self, n=0):
        self.adjacency_matrix = np.zeros((n, n))
        self.n = n
        self.vertices = []
        self.edges = []

        for i in range(0, n):
            self.vertices.append(UndirectedGraphVertex(i + 1))

        for i in range(0, n):
            for j in range(i + 1, n):
                if randint(1, 10) <= 6:
                    self.adjacency_matrix[i, j] = 1
                    self.adjacency_matrix[j, i] = 1

    def to_string(self):
        for i in range(0, self.n):
            for j in range(0, self.n):
                print(self.adjacency_matrix[i, j], end=' ')
            print('\n')