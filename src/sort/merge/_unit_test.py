import sys

from hamcrest import assert_that, equal_to

from . import main


def test_merge_happy():
    arr = [28, 15, 35, 55, 3, 5, 7, 9, 2, 4, 6, 8, 33, 44, 55, 66]
    main.merge(arr, 4, 7, 11)
    assert_that(arr, equal_to([28, 15, 35, 55, 2, 3, 4, 5, 6, 7, 8, 9, 33, 44, 55, 66]))


def test_merge_sort_works():
    input_value = [5, 3, 17, 10, 84, 19, 6, 22, 9]
    main.sort(input_value)
    assert_that(input_value, equal_to([3, 5, 6, 9, 10, 17, 19, 22, 84]))
