import unittest

from union_find import (
    Node,
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
        self.assertEqual(union_find_1.find_set(Node(4)), None)

        vertex_1 = UndirectedGraphVertex(4)
        representative_1 = union_find_1.make_set(vertex_1)
        vertex_2 = UndirectedGraphVertex(6)
        representative_2 = union_find_1.make_set(vertex_2)
        first_set = union_find_1.sets[0]
        second_set = union_find_1.sets[1]

        self.assertEqual(union_find_1.find_set(representative_1), first_set)
        self.assertEqual(union_find_1.find_set(representative_2), second_set)
        self.assertEqual(union_find_1.find_set(Node(4)), None)

    def test_union(self):
        union_find_1 = UnionFind()
        vertex_1 = UndirectedGraphVertex(4)
        representative_1 = union_find_1.make_set(vertex_1)
        vertex_2 = UndirectedGraphVertex(6)
        representative_2 = union_find_1.make_set(vertex_2)

        union_find_1.union_set(representative_1, representative_2)
        self.assertEqual(representative_1.vertex.key, 4)
        self.assertEqual(representative_1.next.vertex.key, 6)


class TestUnionFindList(unittest.TestCase):
    def test_find_element(self):
        vertex = UndirectedGraphVertex(4)
        list_1 = UnionFindList(Node(vertex))
        self.assertEqual(list_1.find_element(vertex), True)


if __name__ == '__main__':
    unittest.main()
