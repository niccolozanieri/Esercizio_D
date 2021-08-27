import unittest
import io
import sys
import random
import numpy as np

from undirected_graph import UndirectedGraph
from undirected_graph_edge import UndirectedGraphEdge
from undirected_graph_vertex import UndirectedGraphVertex


class MainTest(unittest.TestCase):
    def test_ctor(self):
        graph = UndirectedGraph(3)
        graph.initialize(0)
        self.assertEqual(graph.find_edge(UndirectedGraphEdge(graph.vertices[0], graph.vertices[1])), True)
        self.assertEqual(graph.find_edge(UndirectedGraphEdge(graph.vertices[1], graph.vertices[2])), True)
        self.assertEqual(graph.adjacency_matrix.shape, (3, 3))

        vertices = []
        for i in range(0, 4):
            vertices.append(UndirectedGraphVertex(i))

        edges = [UndirectedGraphEdge(vertices[0], vertices[3])]
        graph = UndirectedGraph(4, vertices, edges)
        self.assertEqual(graph.find_edge(UndirectedGraphEdge(graph.vertices[0], graph.vertices[3])), True)
        self.assertEqual(graph.adjacency_matrix[0, 3], 1)
        self.assertEqual(graph.adjacency_matrix[3, 0], 1)

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


class TestConnecteComponents(unittest.TestCase):
    def test_connected_components(self):
        vertices = []
        for i in range(0, 4):
            vertices.append(UndirectedGraphVertex(i))

        edges = [UndirectedGraphEdge(vertices[0], vertices[3])]
        graph = UndirectedGraph(4, vertices, edges)

        connected_components = graph.connected_components()
        captured_output = io.StringIO()
        sys.stdout = captured_output
        connected_components.to_string()
        sys.stdout = sys.__stdout__
        printed_string = '{0, 3} {1} {2} \n'
        self.assertEqual(captured_output.getvalue(), printed_string)


if __name__ == '__main__':
    unittest.main()