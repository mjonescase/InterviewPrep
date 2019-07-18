import sys
import typing

from ..selection.main import Number


def merge(arr: typing.List[Number], p: int, q: int, r: int) -> None:
    """
    Merges two sorted, adjacent sub-arrays of `arr`.
    :param arr: the array containing the sorted sub-arrays
    :param p: the starting index of the leftmost sub-array
    :param q: the last index of the leftmost sub-array
    : param r: the last index of the rightmost sub-array
    """
    left_subarray = append_infinity(arr[p : q + 1])
    right_subarray = append_infinity(arr[q + 1 : r + 1])
    right_index = left_index = 0
    for i in range(p, r + 1):
        if left_subarray[left_index] <= right_subarray[right_index]:
            arr[i] = left_subarray[left_index]
            left_index += 1
        else:
            arr[i] = right_subarray[right_index]
            right_index += 1


append_infinity = lambda x: [*x, sys.maxsize]
