class Node:
    def __init__(self, x, representative=None, next_item=None):
        self.vertex = x
        self.representative = representative
        self.next = next_item


class UnionFindList:
    def __init__(self, representative):
        self.head = representative
        self.tail = representative

    def find_element(self, vertex):
        def _find_element(node):
            if node is None:
                return False
            elif node.vertex.key == vertex.key:
                return True
            else:
                return _find_element(node.next)
        return _find_element(self.head)

    def to_string(self):
        print('{', end='')

        def _to_string(node):
            if node is not None:
                if node.next is not None:
                    print(str(node.vertex.key), end=', ')
                else:
                    print(str(node.vertex.key), end='')
                _to_string(node.next)
            else:
                print('}', end='')
        _to_string(self.head)


class UnionFind:
    def __init__(self):
        self.sets = []

    def make_set(self, vertex):
        node = Node(vertex)
        new_set = UnionFindList(node)
        new_set.head.representative = new_set
        self.sets.append(new_set)

        return node

    def find_set(self, node):
        return node.representative

    def union_set(self, first_node, second_node):
        first_representative = self.find_set(first_node)
        second_representative = self.find_set(second_node)

        first_representative.tail.next = second_representative.head
        current_node = second_representative.head

        while current_node is not None:
            current_node.representative = first_representative
            current_node = current_node.next

        self.sets.remove(second_representative)

    def to_string(self):
        for item in self.sets:
            item.to_string()
            print(' ', end='')
        print('')

