""" https://www.codewars.com/kata/5a4bdd73d8e145f17d000035 """
from unittest import TestCase
from itertools import chain


def sort_nested_list(A: list):
    sorted_numbers = sorted(list(chain.from_iterable(chain.from_iterable(A))))

    for i in A:
        for j in i:
            for q in range(len(j)):
                j[q] = sorted_numbers.pop(0)

    return A


class Testing(TestCase):
    def test_all(self):
        A = [[[]]]
        expected = [[[]]]
        self.assertEqual(sort_nested_list(A), expected)

        A = [[[3, 2, 1]]]
        expected = [[[1, 2, 3]]]
        self.assertEqual(sort_nested_list(A), expected)

        A = [[[2, 1], [4, 3]], [[6, 5], [8, 7]]]
        E = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
        self.assertEqual(sort_nested_list(A), E)

        A = [[[15, 30, 92]]]
        E2 = [[[15, 30, 92]]]
        self.assertEqual(sort_nested_list(A), E2)

        A = [[[82, 87], [47, 44]], [[70, 94], [40, 64]]]
        E3 = [[[40, 44], [47, 64]], [[70, 82], [87, 94]]]
        self.assertEqual(sort_nested_list(A), E3)

        A = [[[29, 32], [82, 61], [75, 91]], [[69, 99], [74, 23], [70, 97]]]
        E4 = [[[23, 29], [32, 61], [69, 70]], [[74, 75], [82, 91], [97, 99]]]
        self.assertEqual(sort_nested_list(A), E4)
