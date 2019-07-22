from hamcrest import assert_that, calling, equal_to, raises

from . import main


def test_parent_index_lt_0():
    assert_that(calling(main.parent).with_args(-5, 2), raises(AssertionError))


def test_parent_ary_lt_0():
    assert_that(calling(main.parent).with_args(3, -3), raises(AssertionError))
