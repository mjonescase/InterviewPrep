from hamcrest import assert_that, equal_to

from . import main


def assert_sorts_as_expected(example: list, expected: list) -> None:
    main.sort(example)
    assert_that(example, equal_to(expected))


def test_sort_simple_example():
    assert_sorts_as_expected([3, 1, 7, 5], [1, 3, 5, 7])


def test_sort_empty_list():
    assert_sorts_as_expected([], [])
