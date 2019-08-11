from .Node import Node


class BinarySearchTree(object):
    """
    Binary search tree implementation in which the
    keys are integers.
    """

    NIL_NODE = None
    root: Node

    def __init__(self) -> "BinarySearchTree":
        self.root = None

    def _create_node(self, key: int) -> Node:
        return Node(key)

    def insert(self, key: int) -> Node:
        """
        Creates a new `Node` with key `key`.
        Inserts this node into this BST while maintaining
        the BST property. Returns the newly inserted `Node`.
        """
        node_to_insert = self._create_node(key)
        node_to_insert.parent = node_to_insert.find_parent(self.root)
        if node_to_insert.parent is self.NIL_NODE:
            self.root = node_to_insert
        elif node_to_insert.key < node_to_insert.parent.key:
            node_to_insert.parent.left = node_to_insert
        else:
            node_to_insert.parent.right = node_to_insert

        return node_to_insert

    def search(self, key: int) -> Node:
        if self.root is None:
            return self.root

        return self.root.search(key)

    @property
    def maximum(self) -> Node:
        if self.root is None:
            return None

        return self.root.maximum

    @property
    def minimum(self) -> Node:
        if self.root is None:
            return None

        return self.root.minimum

    def transplant(self, old_node: Node, new_node: Node) -> None:
        """
        Replace `old_node` with `new_node`.
        `new_node` will now refer to `old_node`'s parent as its
        parent, and will take whichever of the parent's child slots
        that `old_node` occupied, either left or right.
        """
        if old_node == self.root:
            self.root = new_node
        else:
            old_node.transplant(new_node)

    def delete(self, node: Node) -> None:
        if node.left is self.NIL_NODE:
            self.transplant(node, node.right)
        elif node.right is self.NIL_NODE:
            self.transplant(node, node.left)
        else:
            successor = node.right.minimum
            if successor.parent != node:
                successor.transplant(successor.right)
                successor.right = node.right
                successor.right.parent = successor

            node.transplant(successor)
            successor.left = node.left
            successor.left.parent = successor
