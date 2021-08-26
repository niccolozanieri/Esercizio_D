class UndirectedGraphEdge:
    def __init__(self, first_vertex, second_vertex, weight=1):
        self.first_vertex = first_vertex
        self.second_vertex = second_vertex
        self.weight = weight

    def is_equal(self, right):
        partial_1 = self.first_vertex == right.first_vertex and self.second_vertex == right.second_vertex
        partial_2 = self.first_vertex == right.second_vertex and self.second_vertex == right.first_vertex
        return partial_1 or partial_2
