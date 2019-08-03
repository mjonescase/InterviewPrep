from hamcrest import assert_that, calling, greater_than_or_equal_to, less_than, raises

from .HashTable import HashTable
from .HashTableFullException import HashTableFullException


def test_insert_none():
    table = HashTable(5)
    assert_that(calling(table.insert).with_args(None), raises(ValueError))


def test_insert_full():
    table = HashTable(5)
    _ = [table.insert(i) for i in range(5)]
    assert_that(calling(table.insert).with_args(6), raises(HashTableFullException))


def test_insert_happy():
    table = HashTable(5)
    index = table.insert(8)
    assert_that(index, less_than(table.size))
    assert_that(index, greater_than_or_equal_to(0))
