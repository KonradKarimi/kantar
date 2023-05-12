def sort_numbers(numbers: list[int]) -> list[int]:
    """

    :param numbers: list of numbers
    :return: list of numbers in ascending order
    """
    return sorted(numbers)


def reverse_sort_numbers(numbers: list[int]) -> list[int]:
    """
    :param numbers: list of numbers
    :return: list of numbers in reverse order
    """
    return list(reversed(sorted(numbers)))
