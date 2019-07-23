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


def max_heapify(heap: typing.List[int], index: int, heap_size: int) -> None:
    """
    Modifies `heap` in place

    :param heap: A binary heap
    :param index: the root of the sub-heap to max heapify
    :param heap_size: the size of the heap within the array `heap`
    """
    assert index < len(heap)
    assert index >= 0
    assert heap_size >= 0
    assert heap_size <= len(heap)
    largest = index
    for i in range(2):
        ith_index = ith_child(index, 2, i)
        if ith_index < heap_size and heap[ith_index] > heap[largest]:
            largest = ith_index

    if largest != index:
        temp = heap[index]
        heap[index] = heap[largest]
        heap[largest] = temp
        max_heapify(heap, largest, heap_size)


def build_max_heap(arr: typing.List[int]) -> None:
    """
    Max-heapifies `arr`.
    """
    [
        max_heapify(arr, i, len(arr))
        for i in range(max(math.floor(len(arr) / 2) - 1, 0), -1, -1)
    ]
