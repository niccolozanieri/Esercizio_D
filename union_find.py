class UnionFindList:
    def __init__(self, representative):
        self.head = representative
        self.tail = representative

    def to_string(self):
        print('{', end='')

        def _to_string(node):
            if node is not None:
                if node.next is not None:
                    print(str(node.key), end=', ')
                else:
                    print(str(node.key), end='')
                _to_string(node.next)
            else:
                print('}', end='')
        _to_string(self.head)


class UnionFind:
    def __init__(self):
        self.sets = []

    def make_set(self, vertex):
        new_set = UnionFindList(vertex)
        vertex.representative = new_set
        vertex.next = None
        self.sets.append(new_set)

        return vertex

    def find_set(self, vertex):
        return vertex.representative

    def union(self, first_vertex, second_vertex):
        first_representative = self.find_set(first_vertex)
        second_representative = self.find_set(second_vertex)

        first_representative.tail.next = second_representative.head
        first_representative.tail = second_representative.tail
        current_vertex = second_representative.head

        while current_vertex is not None:
            current_vertex.representative = first_representative
            current_vertex = current_vertex.next

        self.sets.remove(second_representative)

    def to_string(self):
        for item in self.sets:
            item.to_string()
            print(' ', end='')
        print('')

