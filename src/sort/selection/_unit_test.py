import copy
from decimal import Decimal
from unittest.mock import Mock, call, patch
import typing

from hamcrest import assert_that, equal_to, none

from . import main


def test_find_smallest_index_empty():
    """
    Document the behavior when an empty list is sent in.
    """
    assert_that(main.find_smallest_index([]), none())


def test_find_smallest_index_happy():
    """
    Make sure `find_smallest_index` finds the
    array index with the smallest value with a
    straightforward, small, typical example input.
    """
    assert_that(main.find_smallest_index([4, 7, 3, 9]), equal_to(2))


def test_find_smallest_index_non_decreasing():
    """
    Show that `find_smallest_index` deals with ties
    by going with the first index of the value
    that it finds.
    """
    assert_that(main.find_smallest_index([4, 7, 3, 3, 9]), equal_to(2))


def test_find_smallest_index_already_sorted():
    assert_that(main.find_smallest_index([2, 3, 5, 7]), equal_to(0))


def test_find_smallest_index_handles_all_types():
    """
    Make sure comparing all the numeric types in Python
    works as expected.
    """
    assert_that(
        main.find_smallest_index([4, 4.0, Decimal("4.0"), Decimal(4), Decimal(4.0)]),
        equal_to(0),
    )


def test_sort_empty_list():
    """
    Make sure that, when sent an empty list,
    an empty list is returned.
    """
    initial_list = []
    main.sort(initial_list)
    assert_that(initial_list, equal_to([]))


def test_sort_already_sorted():
    """
    Handle a simple case.
    """
    initial_list = [2, 3, 5, 7]
    main.sort(initial_list)
    assert_that(initial_list, equal_to([2, 3, 5, 7]))


def test_already_sorted_calls_helper():
    initial_list = [*range(5)]
    _test_sort_calls_helper(
        0,
        initial_list,
        initial_list,
        [call(initial_list[i:]) for i in range(len(initial_list) - 1)],
    )


def test_first_becomes_last_calls_helper():
    initial_list = [*range(5)]
    _test_sort_calls_helper(
        1,
        initial_list,
        [*range(1, 5), 0],
        [call([0, *initial_list[i:]]) for i in range(2, len(initial_list))],
    )


def _test_sort_calls_helper(
    smallest_index: int,
    initial_list: typing.List[main.Number],
    expected_result: typing.List[main.Number],
    calls: typing.List["call"],
):
    """
    Make sure `sort` calls `find_smallest_index`
    a total of `len(arr) - 1` times.

    Also make sure it does what it's supposed to do with
    `find_smallest_index`'s return value.

    :param smallest_index: what does `find_smallest_index` always return?
    :param initial_list: what should be passed into `sort`?
    :param expected_result: what should `sort` return?
    """
    # TODO struggled mightily to patch a function in a
    # module that's relatively imported.
    # pytest_mocker doesn't appear to support `patch_object`.
    original_find_smallest = main.find_smallest_index
    initial_list_copy = copy.deepcopy(initial_list)
    try:
        main.find_smallest_index = Mock(return_value=smallest_index)
        main.sort(initial_list)
        assert_that(initial_list, equal_to(expected_result))
        main.find_smallest_index.assert_has_calls(calls)
    finally:
        main.find_smallest_index = original_find_smallest
