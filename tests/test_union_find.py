import unittest
import io
import sys

from union_find import (
    UnionFind,
    UnionFindList
)
from undirected_graph_vertex import UndirectedGraphVertex


class TestUnionFind(unittest.TestCase):
    def test_make_set(self):
        union_find_1 = UnionFind()
        self.assertEqual(union_find_1.sets, [])

        vertex = UndirectedGraphVertex(4)
        representative_1 = union_find_1.make_set(vertex)
        first_set = union_find_1.sets[0]
        self.assertEqual(first_set is None, False)
        self.assertEqual(first_set.head, representative_1)
        self.assertEqual(first_set.tail, representative_1)
        self.assertEqual(first_set.head.representative, first_set)

    def test_find_set(self):
        union_find_1 = UnionFind()
        self.assertEqual(union_find_1.find_set(UndirectedGraphVertex(4)), None)

        vertex_1 = UndirectedGraphVertex(4)
        representative_1 = union_find_1.make_set(vertex_1)
        vertex_2 = UndirectedGraphVertex(6)
        representative_2 = union_find_1.make_set(vertex_2)
        first_set = union_find_1.sets[0]
        second_set = union_find_1.sets[1]

        self.assertEqual(union_find_1.find_set(representative_1), first_set)
        self.assertEqual(union_find_1.find_set(representative_2), second_set)
        self.assertEqual(union_find_1.find_set(UndirectedGraphVertex(4)), None)

    def test_union(self):
        union_find_1 = UnionFind()
        vertex_1 = union_find_1.make_set(UndirectedGraphVertex(4))
        vertex_2 = union_find_1.make_set(UndirectedGraphVertex(6))

        union_find_1.union(vertex_1, vertex_2)
        self.assertEqual(vertex_1.key, 4)
        self.assertEqual(vertex_1.next.key, 6)

        vertex_3 = union_find_1.make_set(UndirectedGraphVertex(3))
        vertex_4 = union_find_1.make_set(UndirectedGraphVertex(9))
        union_find_1.union(vertex_2, vertex_4)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        union_find_1.to_string()
        sys.stdout = sys.__stdout__
        printed_string = '{4, 6, 9} {3} \n'
        self.assertEqual(captured_output.getvalue(), printed_string)


if __name__ == '__main__':
    unittest.main()
