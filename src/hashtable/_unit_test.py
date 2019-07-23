from hamcrest import assert_that, greater_than_or_equal_to, less_than

from .HashTable import HashTable

table = HashTable(5)


def test_hash_this_happy():
    index = table.hash_this("a")
