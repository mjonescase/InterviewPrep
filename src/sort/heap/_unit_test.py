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
