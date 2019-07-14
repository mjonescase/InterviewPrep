import sys
import typing

Number = typing.Union[int, float, "decimal.Decimal"]


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
