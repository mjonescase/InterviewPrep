class HashTableFullException(Exception):
    def __init__(self):
        return super().__init__(
            "This hashtable is already full. Item could not be inserted."
        )
