class UndirectedGraphVertex:
    def __init__(self, key):
        self.key = key

    def is_equal(self, right):
        return self.key == right.key
