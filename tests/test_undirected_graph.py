import unittest
import io
import sys
import random
import numpy as np

from undirected_graph import UndirectedGraph
from undirected_graph_edge import UndirectedGraphEdge


class MainTest(unittest.TestCase):
    def test_ctor(self):
        graph = UndirectedGraph(3)
        graph.initialize(0)
        self.assertEqual(graph.find_edge(UndirectedGraphEdge(graph.vertices[0], graph.vertices[1])), True)
        self.assertEqual(graph.find_edge(UndirectedGraphEdge(graph.vertices[1], graph.vertices[2])), True)
        self.assertEqual(graph.adjacency_matrix.shape, (3, 3))

    def test_to_string(self):
        graph = UndirectedGraph()
        captured_output = io.StringIO()
        sys.stdout = captured_output
        graph.to_string()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), '')

        graph = UndirectedGraph(3)
        graph.initialize(0)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        graph.to_string()
        sys.stdout = sys.__stdout__
        printed_matrix = '0 1 0 \n1 0 1 \n0 1 0 \n'
        self.assertEqual(captured_output.getvalue(), printed_matrix)


if __name__ == '__main__':
    unittest.main()