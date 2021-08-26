import unittest
from undirected_graph_vertex import UndirectedGraphVertex


class MainTest(unittest.TestCase):
    def test_is_equal(self):
        vertex_1 = UndirectedGraphVertex(3)
        vertex_2 = UndirectedGraphVertex(3)
        vertex_3 = UndirectedGraphVertex(4)

        self.assertEqual(vertex_1.is_equal(vertex_2), True)
        self.assertEqual(vertex_1.is_equal(vertex_1), True)
        self.assertEqual(vertex_1.is_equal(vertex_3), False)


if __name__ == '__main__':
    unittest.main()