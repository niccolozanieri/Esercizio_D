import unittest
import io
import sys
import random

from undirected_graph import UndirectedGraph


class MainTest(unittest.TestCase):
    def test_to_string(self):
        graph = UndirectedGraph()
        captured_output = io.StringIO()
        sys.stdout = captured_output
        graph.to_string()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), '')


if __name__ == '__main__':
    unittest.main()