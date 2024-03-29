import copy
import sys
import typing

Number = typing.Union[int, float, "decimal.Decimal"]


def sort(arr: typing.List[Number]) -> typing.List[Number]:
    """
    Sorts a list of numbers, using the Selection Sort algorithm.

    :param arr: The list to sort.
    """
    for i in range(len(arr) - 1):
        temp_ith_value = arr[i]
        smallest_index = find_smallest_index(arr[i:]) + i
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp_ith_value


def find_smallest_index(arr: typing.List[Number]) -> int:
    """
    :param arr: Find the smallest in this list
    """
    smallest_index: int = None
    smallest_value: Number = sys.maxsize
    for index, value in enumerate(arr):
        if value < smallest_value:
            smallest_value = value
            smallest_index = index

    return smallest_index
