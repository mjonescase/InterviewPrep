from . import algorithms
from .Node import Node


class BinarySearchTree(object):
    """
    Binary search tree implementation in which the
    keys are integers.
    """

    root: Node

    def __init__(self) -> "BinarySearchTree":
        self.root = None

    def insert(self, key) -> None:
        node_to_insert = Node(key)
        node_to_insert.parent = algorithms.find_parent(self.root, node_to_insert)
        if node_to_insert.parent is None:
            self.root = node_to_insert
        elif node_to_insert.key < node_to_insert.parent.key:
            node_to_insert.parent.left = node_to_insert
        else:
            node_to_insert.parent.right = node_to_insert

    def search(self, key: int) -> Node:
        return algorithms.search(self.root, key)

    @property
    def maximum(self) -> Node:
        if self.root is None:
            return None

        return algorithms.maximum(self.root)

    @property
    def minimum(self) -> Node:
        if self.root is None:
            return None

        return algorithms.minimum(self.root)
