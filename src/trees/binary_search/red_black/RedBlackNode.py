from ..Node import Node
from .Color import Color
from .NilNode import NIL_NODE


class RedBlackNode(Node):
    """
    A node in a red-black tree. A Red-black tree has these properties:
    - Every node is either red or black.
    - The root is black.
    - every leaf (NIL) is black.
    - If a node is red, then both its children are black.
    - For each node, all simple paths from the node to descendant leaves have the same number of black nodes.
    """

    NIL_NODE = NIL_NODE
    parent: "RedBlackNode"
    left: "RedBlackNode"
    right: "RedBlackNode"
    color: Color

    def __init__(
        self,
        key: int,
        color: Color,
        parent: "RedBlackNode" = None,
        left: "RedBlackNode" = None,
        right: "RedBlackNode" = None,
    ):
        self.key = key
        self.color = color
        self.parent = parent if parent is not None else self.NIL_NODE
        self.left = left if left is not None else self.NIL_NODE
        self.right = right if right is not None else self.NIL_NODE

    @property
    def uncle(self) -> "RedBlackNode":
        """
        Returns my parent's parent's child that is not my parent.
        """
        return self.NIL_NODE
        # grandparent = self.parent.parent
        # if self.parent is self.parent.parent.right:
        #     return self.parent.parent.left

        # return self.parent.parent.right
