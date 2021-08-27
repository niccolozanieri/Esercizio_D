class UndirectedGraphVertex:
    def __init__(self, key):
        self.key = key
        self.representative = None
        self.next = None

    def is_equal(self, right):
        return self.key == right.key
