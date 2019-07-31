from hamcrest import assert_that, calling, greater_than_or_equal_to, less_than, raises

from .HashTable import HashTable


def test_hash_none():
    table = HashTable(5)
    assert_that(calling(table.insert).with_args(None), raises(ValueError))
