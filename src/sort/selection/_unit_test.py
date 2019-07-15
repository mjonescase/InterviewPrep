from decimal import Decimal
from unittest.mock import Mock, call, patch

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
    assert_that(main.sort([]), equal_to([]))


def test_sort_already_sorted():
    """
    Handle a simple case.
    """
    assert_that(main.sort([2, 3, 5, 7]), equal_to([2, 3, 5, 7]))


def test_sort_calls_helper():
    """
    Make sure `sort` calls `find_smallest_index`
    a total of `len(arr) - 1` times.

    Also make sure it does what it's supposed to do with
    `find_smallest_index`'s return value.
    """
    arr = range(5)
    # TODO struggled mightily to patch a function in a
    # module that's relatively imported.
    # pytest_mocker doesn't appear to support `patch_object`.
    original_find_smallest = main.find_smallest_index
    try:
        main.find_smallest_index = Mock(return_value=0)
        assert_that(main.sort(arr), equal_to(arr))
        main.find_smallest_index.assert_has_calls([call(range(i, 5)) for i in range(4)])
    finally:
        main.find_smallest_index = original_find_smallest
