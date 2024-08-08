import unittest

from parameterized import parameterized

from main import Stack


class TestStringMethods(unittest.TestCase):

    @parameterized.expand(
        [
            [[1, 2, 3, 4, 5], [(5, 5), (4, 4), (3, 3), (2, 2), (1, 1)]],
            [[5, 4, 3, 2, 1], [(5, 1), (5, 2), (5, 3), (5, 4), (5, 5)]],
            [[1, 3, 5, 4, 2], [(5, 2), (5, 4), (5, 5), (3, 3), (1, 1)]],
            [[2, 4, 1, 3, 5], [(5, 5), (4, 3), (4, 1), (4, 4), (2, 2)]],
        ]
    )
    def test(self, items: list[int], max_and_pop_list: list[tuple[int, int]]):
        stack = Stack()
        for i in items:
            stack.insert(i)

        for t_max, popped in max_and_pop_list:
            self.assertEqual(stack.max(), t_max)
            self.assertEqual(stack.pop(), popped)


if __name__ == '__main__':
    unittest.main()
