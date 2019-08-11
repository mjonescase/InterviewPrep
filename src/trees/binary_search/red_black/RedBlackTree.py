from ..BinarySearchTree import BinarySearchTree
from .Color import Color
from .NilNode import NIL_NODE
from .RedBlackNode import RedBlackNode


class RedBlackTree(BinarySearchTree):
    """
    A Red-Black Tree is one implementation of a balanced binary tree.
    """

    # `NIL_NODE` is a sentinel. It serves to "fill out" any unfilled leaves of the tree. It is also the parent of the root of the tree.
    NIL_NODE = NIL_NODE
    root: RedBlackNode

    def _create_node(self, key: int) -> RedBlackNode:
        return RedBlackNode(key, color=Color.RED)

    # def insert(self, key: int) -> RedBlackNode:
    #     return super().insert(key)

    def left_rotate(self, node: RedBlackNode) -> None:
        right_child = node.right
        # turn right child's left subtree into node's right subtree
        node.right = right_child.left
        if right_child.left != self.NIL_NODE:
            right_child.left.parent = node

        right_child.parent = node.parent
        if node.parent is self.NIL_NODE:
            self.root = right_child
        elif node.parent.left is node:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        node.parent = right_child
        right_child.left = node

    def right_rotate(self, node: RedBlackNode) -> None:
        left_child = node.left
        # turn left child's right subtree into node's left subtree
        node.left = left_child.right
        if left_child.right != self.NIL_NODE:
            left_child.right.parent = node

        left_child.parent = node.parent
        if node.parent is self.NIL_NODE:
            self.root = left_child
        elif node.parent.left is node:
            node.parent.left = left_child
        else:
            node.parent.right = left_child

        node.parent = left_child
        left_child.right = node
