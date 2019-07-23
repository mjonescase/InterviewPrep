from unittest.mock import MagicMock

from hamcrest import assert_that, calling, equal_to, raises

from . import main


def test_parent_index_lt_0():
    assert_that(calling(main.parent).with_args(-5, 2), raises(AssertionError))


def test_parent_ary_lt_0():
    assert_that(calling(main.parent).with_args(3, -3), raises(AssertionError))


def test_parent_happy():
    assert_that(main.parent(1, 2), equal_to(0))


def test_ith_child_index_lt_0():
    assert_that(
        calling(main.ith_child).with_args(-1, MagicMock(), MagicMock()),
        raises(AssertionError),
    )


def test_ith_child_ith_lt_0():
    assert_that(
        calling(main.ith_child).with_args(0, MagicMock(), -1), raises(AssertionError)
    )


def test_ith_child_ith_gte_ary():
    assert_that(calling(main.ith_child).with_args(0, 2, 2), raises(AssertionError))


def test_ith_child_ary_lte_1():
    assert_that(calling(main.ith_child).with_args(0, 1, 0), raises(AssertionError))


def test_ith_child_happy():
    assert_that(main.ith_child(0, 2, 1), equal_to(2))


def test_max_heapify_index_gte_heap_length():
    assert_that(calling(main.max_heapify).with_args([], 0, 0), raises(AssertionError))


def test_max_heapify_index_lt_0():
    assert_that(calling(main.max_heapify).with_args([], -1, 0), raises(AssertionError))


def test_max_heapify_heap_size_lt_0():
    assert_that(
        calling(main.max_heapify).with_args([MagicMock()], 0, -1),
        raises(AssertionError),
    )


def test_max_heapify_heap_size_lt_0():
    assert_that(
        calling(main.max_heapify).with_args([MagicMock()], 0, 2), raises(AssertionError)
    )


def test_max_heapify_works():
    input_value = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    main.max_heapify(input_value, 3, len(input_value))
    assert_that(input_value), equal_to([27, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3, 0])
