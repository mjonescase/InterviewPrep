from .Node import Node


class BinarySearchTree(object):
    """
    Binary search tree implementation in which the
    keys are integers.
    """

    root: Node

    def __init__(self, root_key: int) -> "BinarySearchTree":
        self.root = Node(key=root_key)

    def insert(self, key) -> None:
        if key < self.root.key:
            self.root.left = Node(key=key, parent=self.root)
        else:
            # Per the convention in CLRS chapter 12.3,
            # right wins in a tie (keys are equal)
            self.root.right = Node(key=key, parent=self.root)
