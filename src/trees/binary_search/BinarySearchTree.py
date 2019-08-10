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
        parent = None
        insert_point = self.root
        while insert_point:
            parent = insert_point
            if key < insert_point.key:
                # Per the convention in CLRS chapter 12.3,
                # right wins in a tie (keys are equal)
                insert_point = insert_point.left
            else:
                insert_point = insert_point.right

        node_to_insert.parent = parent
        if parent is None:
            self.root = node_to_insert
        elif node_to_insert.key < parent.key:
            parent.left = node_to_insert
        else:
            parent.right = node_to_insert
