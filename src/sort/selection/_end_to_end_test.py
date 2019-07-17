from hamcrest import assert_that, equal_to

from . import main


def assert_sorts_as_expected(example: list, expected: list) -> None:
    assert_that(main.sort(example), equal_to(expected))


def test_sort_simple_example():
    assert_sorts_as_expected([3, 1, 7, 5], [1, 3, 7, 5])


def test_sort_empty_list():
    assert_sorts_as_expected([], [])
