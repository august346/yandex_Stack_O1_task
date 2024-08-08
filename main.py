from typing import Any


# все методы должны быть не сложнее O(1)
# class Stack:
#     def __init__(self):
#         pass
#
#     def insert(self, elem):
#         pass
#
#     def pop(self):
#         pass
#
#     def max(self):
#         pass


class Stack:
    storage: list
    maximums: list[tuple[int, Any]]

    def __init__(self):
        self.storage = []
        self.maximums = []

    def insert(self, elem):
        self.storage.append(elem)
        ind = len(self.storage) - 1
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
