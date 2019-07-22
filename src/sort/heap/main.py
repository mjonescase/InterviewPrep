import math
import typing


def parent(index: int, ary: int) -> int:
    """
    Return the index's parent index in a zero-indexed,
    `ary`-ary heap.
    """
    assert index > 0
    assert ary > 1  # a 1-ary heap is just a linked list. Not interested!
    return math.floor((index - 1) / ary)


def ith_child(index: int, ary: int, ith: int) -> int:
    """
    Return the index's `ith` child (zero-indexed) in a zero-indexed,
    `ary`-ary heap.
    """
    assert index >= 0
    assert ith >= 0
    assert ary > 1
    assert ith < ary
    return ary * index + ith + 1


def max_heapify(heap: typing.List[int], index: int) -> None:
    """
    Modifies `heap` in place
    """
