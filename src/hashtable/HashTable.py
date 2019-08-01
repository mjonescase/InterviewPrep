import typing

NONE_ERROR_MESSAGE = "Storing `None` is not supported by this hashtable implementation"


class HashTable(object):
    """
    Implements a hashtable in Python using only an array.
    Uses the built-in `hash` function, which limits
    this class for use only with "hashable" objects -- 
    that is, objects whose classes have implemented
    `__hash__()`.

    This implementation handles collisions using Open Addressing.
    """

    size: int
    _table: typing.List

    def __init__(self, size: int):
        self.size = size
        self._table = [None for _ in range(size)]
        self._num_elements = 0

    def _hash_this(self, val: typing.Hashable, try_number: int = 0) -> int:
        """
        given any hashable object, return its
        key (array index) in this hashtable.

        :param val: the value being inserted.
        :param try_number: In Open Addressing, collisions are resolved
        by trying another slot in a systematic way.
        The hashing algorithm must satisfy the property that, for any
        given `val`, every slot in the table (every array index)
        must potentially be considered as a slot until the table fills up.
        `try_number` is in the range [0, self.size-1].

        TODO: the `+ try_number` bit amounts to "linear probing", which
        suffers from Primary Clustering, or long runs of occupied slots.

        To use quadratic probing or double hashing, i would need to introduce
        one or more "auxiliary" hash functions.
        """
        return (abs(hash(val)) + try_number) % self.size

    def insert(self, val: typing.Hashable) -> int:
        """
        Find an available slot for `val`, a hashable object,
        in this hashtable, and insert it there.

        Returns the index at which the value was inserted.
        """
        if val is None:
            raise ValueError(NONE_ERROR_MESSAGE)

        for try_number in range(self.size):
            index = self._hash_this(val, try_number)
            if self._table[index] is None:
                self._table[index] = val
                return index
        else:
            raise OverflowError(
                "This hashtable is already full. Item could not be inserted."
            )

    def search(self, val: typing.Hashable) -> int:
        if val is None:
            raise ValueError(NONE_ERROR_MESSAGE)

        for try_number in range(self.size):
            index = self._hash_this(val, try_number)
            if self._table[index] == val:
                return index
        else:
            raise KeyError(str(val))
