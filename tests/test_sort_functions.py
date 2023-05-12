import unittest
from service.sort_service import sort_numbers, reverse_sort_numbers


class TestSortFunctions(unittest.TestCase):
    """
    Tests for the sorting functionality.
    """

    def test_sort_numbers(self):
        numbers = [4, 2, 1, 3]
        sorted_numbers = sort_numbers(numbers)
        self.assertEqual(sorted_numbers, [1, 2, 3, 4])

    def test_reverse_sort_numbers(self):
        numbers = [4, 2, 1, 3]
        reverse_sorted_numbers = reverse_sort_numbers(numbers)
        self.assertEqual(reverse_sorted_numbers, [4, 3, 2, 1])

    def test_sort_numbers_with_negative_numbers(self):
        numbers = [4, -2, 1, 3]
        sorted_numbers = sort_numbers(numbers)
        self.assertEqual(sorted_numbers, [-2, 1, 3, 4])

    def test_reverse_sort_numbers_with_negative_numbers(self):
        numbers = [4, -2, 1, 3]
        reverse_sorted_numbers = reverse_sort_numbers(numbers)
        self.assertEqual(reverse_sorted_numbers, [4, 3, 1, -2])

    def test_sort_numbers_with_float_numbers(self):
        numbers = [4, 2.5, 1, 3]
        sorted_numbers = sort_numbers(numbers)
        self.assertEqual(sorted_numbers, [1, 2.5, 3, 4])

    def test_reverse_sort_numbers_with_float_numbers(self):
        numbers = [4, 2.5, 1, 3]
        reverse_sorted_numbers = reverse_sort_numbers(numbers)
        self.assertEqual(reverse_sorted_numbers, [4, 3, 2.5, 1])


if __name__ == '__main__':
    unittest.main()
