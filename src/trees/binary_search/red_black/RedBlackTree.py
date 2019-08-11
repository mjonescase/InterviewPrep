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
        # TODO if node.parent is self.NIL_NODE,
        # right_child is the root of the tree now.
        if node.parent.left is node:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        node.parent = right_child
        right_child.left = node
