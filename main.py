from typing import Any


class Stack:
    storage: list
    maximums: list[tuple[int, Any]]

    def __init__(self):
        self.storage = []
        self.maximums = []

    def insert(self, elem):
        ind = len(self.storage)
        self.storage.append(elem)
        if not self.maximums:
            self.maximums = [(ind, elem)]
        elif self.maximums[-1][1] < elem:
            self.maximums.append((ind, elem))

    def pop(self):
        ind = len(self.storage) - 1
        elem = self.storage.pop()

        if self.maximums[-1][0] == ind:
            self.maximums.pop()

        return elem

    def max(self):
        return self.maximums[-1][1]
