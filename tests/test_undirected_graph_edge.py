import unittest

from undirected_graph_edge import UndirectedGraphEdge
from undirected_graph_vertex import UndirectedGraphVertex


class MainTest(unittest.TestCase):
    def test_is_equal(self):
        vertex_1 = UndirectedGraphVertex(3)
        vertex_2 = UndirectedGraphVertex(5)
        vertex_3 = UndirectedGraphVertex(3)

        edge_1 = UndirectedGraphEdge(vertex_1, vertex_2)
        edge_2 = UndirectedGraphEdge(vertex_1, vertex_2)
        edge_3 = UndirectedGraphEdge(vertex_2, vertex_1)
        edge_4 = UndirectedGraphEdge(vertex_1, vertex_3)
        edge_5 = UndirectedGraphEdge(vertex_1, vertex_1)

        self.assertEqual(edge_1.is_equal(edge_2), True)
        self.assertEqual(edge_2.is_equal(edge_1), True)
        self.assertEqual(edge_1.is_equal(edge_3), True)
        self.assertEqual(edge_1.is_equal(edge_5), False)
        self.assertEqual(edge_4.is_equal(edge_5), False)
        self.assertEqual(edge_4.is_equal(edge_4), True)


if __name__ == '__main__':
    unittest.main()
