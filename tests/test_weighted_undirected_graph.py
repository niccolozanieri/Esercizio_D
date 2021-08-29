import unittest
import io
import sys

from weighted_undirected_graph import WeightedUndirectedGraph
from undirected_graph_vertex import UndirectedGraphVertex
from undirected_graph_edge import UndirectedGraphEdge


class MainTest(unittest.TestCase):
    def setUp(self):
        vertices = []
        for i in range(0, 10):
            vertices.append(UndirectedGraphVertex(i))

        edges = [
            UndirectedGraphEdge(vertices[0], vertices[8], 2),
            UndirectedGraphEdge(vertices[0], vertices[9], 3),
            UndirectedGraphEdge(vertices[8], vertices[2], 4),
            UndirectedGraphEdge(vertices[7], vertices[2], 6),
            UndirectedGraphEdge(vertices[6], vertices[7], 1),
            UndirectedGraphEdge(vertices[6], vertices[3], 2),
            UndirectedGraphEdge(vertices[3], vertices[4], 2),
            UndirectedGraphEdge(vertices[7], vertices[5], 2),
            UndirectedGraphEdge(vertices[4], vertices[5], 3),
            UndirectedGraphEdge(vertices[4], vertices[1], 5)
        ]

        self.graph = WeightedUndirectedGraph(10, vertices, edges)

    def test_edge_quick_sort(self):
        self.graph.edges_quick_sort()

        captured_output = io.StringIO()
        sys.stdout = captured_output
        for edge in self.graph.edges:
            print(f'{edge.weight}', end=' ')
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), '1 2 2 2 2 3 3 4 5 6 ')

    def test_kruskal_mst(self):
        mst_edges = self.graph.kruskal_mst()

        captured_output = io.StringIO()
        sys.stdout = captured_output
        for edge in mst_edges:
            print(f'{edge.first_vertex.key} {edge.second_vertex.key}', end=' : ')
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue(), '6 7 : 0 8 : 6 3 : 3 4 : 7 5 : 0 9 : 8 2 : 4 1 : 7 2 : ')


if __name__ == '__main__':
    unittest.main()
