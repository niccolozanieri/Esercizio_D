import numpy as np
from random import randint

from undirected_graph_vertex import UndirectedGraphVertex
from undirected_graph_edge import UndirectedGraphEdge
from union_find import UnionFind


class UndirectedGraph:
    def __init__(self, n=0, vertices=None, edges=None):
        self.adjacency_matrix = np.zeros((n, n), dtype=np.int16)
        self.n = n

        if vertices is None or edges is None:
            self.vertices = []
            self.edges = []

            for i in range(0, n):
                self.vertices.append(UndirectedGraphVertex(i))
        else:
            self.vertices = vertices
            self.edges = edges
            for edge in edges:
                self.adjacency_matrix[edge.first_vertex.key, edge.second_vertex.key] = 1
                self.adjacency_matrix[edge.second_vertex.key, edge.first_vertex.key] = 1

    def initialize(self, rand=1):
        if rand == 1:
            for i in range(0, self.n):
                for j in range(i + 1, self.n):
                    if randint(1, 10) <= 1:
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

    def connected_components(self):
        components_list = UnionFind()

        for vertex in self.vertices:
            components_list.make_set(vertex)
        for edge in self.edges:
            if components_list.find_set(edge.first_vertex) != components_list.find_set(edge.second_vertex):
                components_list.union(edge.first_vertex, edge.second_vertex)

        return components_list
