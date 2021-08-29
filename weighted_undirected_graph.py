import math
from random import randint

from undirected_graph import UndirectedGraph
from undirected_graph_edge import UndirectedGraphEdge
from union_find import UnionFind


class WeightedUndirectedGraph(UndirectedGraph):
    def __init__(self, n=0, vertices=None, edges=None):
        super().__init__(n, vertices, edges)

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

    @staticmethod
    def swap(seq, a, b):
        tmp = seq[a]
        seq[a] = seq[b]
        seq[b] = tmp

    def edge_partition(self, p, r):
        pivot = self.edges[r].weight
        i = p - 1

        for j in range(p, r):
            if self.edges[j].weight <= pivot:
                i = i + 1
                WeightedUndirectedGraph.swap(self.edges, i, j)
        WeightedUndirectedGraph.swap(self.edges, i + 1, r)

        return i + 1

    def edges_quick_sort(self):
        def _edges_quick_sort(p, r):
            if p < r:
                q = self.edge_partition(p, r)
                _edges_quick_sort(p, q - 1)
                _edges_quick_sort(q + 1, r)

        _edges_quick_sort(0, len(self.edges) - 1)

    def kruskal_mst(self):
        mst_edges = []
        union_find = UnionFind()

        for vertex in self.vertices:
            union_find.make_set(vertex)

        self.edges_quick_sort()
        unions = 0

        for edge in self.edges:
            if union_find.find_set(edge.first_vertex) != union_find.find_set(edge.second_vertex):
                mst_edges.append(edge)
                union_find.union(edge.first_vertex, edge.second_vertex)

                unions += 1
                if unions == len(self.vertices) - 1:
                    break

        return mst_edges
