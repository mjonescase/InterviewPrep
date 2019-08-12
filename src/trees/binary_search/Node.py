class Node(object):
    """
    Represents a node in a binary search tree,
    where the keys are `int`s.
    """

    NIL_NODE = None
    key: int
    parent: "Node"
    left: "Node"
    right: "Node"

    def __init__(
        self, key: int, parent: "Node" = None, left: "Node" = None, right: "Node" = None
    ):
        self.key = key
        self.parent = parent if parent is not None else self.NIL_NODE
        self.left = left if left is not None else self.NIL_NODE
        self.right = right if right is not None else self.NIL_NODE

    @property
    def maximum(self) -> "Node":
        """
        :param node: Node at the root of the tree to be searched.

        Returns the Node in the tree containing the maximum key.
        """
        if self.right is self.NIL_NODE:
            return self

        return self.right.maximum

    @property
    def minimum(self) -> "Node":
        """
        :param node: Node at the root of the tree to be searched.

        Returns the Node in the tree containing the minimum key.
        """
        if self.left is self.NIL_NODE:
            return self

        return self.left.minimum

    @property
    def successor(self) -> "Node":
        """
        Returns the node with the smallest key greater than `self.key`
        """
        if self.right is not self.NIL_NODE:
            return self.right.minimum

        current = self
        parent = self.parent
        while parent is not self.NIL_NODE and current == parent.right:
            current = parent
            parent = parent.parent

        return parent

    @property
    def predecessor(self) -> "Node":
        if self.left is not self.NIL_NODE:
            return self.left.maximum

        current = self
        parent = self.parent
        while parent is not self.NIL_NODE and current == parent.left:
            current = parent
            parent = parent.parent

        return parent

    def find_parent(self, root: "Node") -> "Node":
        """
        :param root: The node at the root of the tree

        Returns the node that should serve as this node's parent.
        """
        parent = None
        insert_point = root
        while insert_point and insert_point is not self.NIL_NODE:
            parent = insert_point
            if self.key < insert_point.key:
                # Per the convention in CLRS chapter 12.3,
                # right wins in a tie (keys are equal)
                insert_point = insert_point.left
            else:
                insert_point = insert_point.right

        return parent if parent is not None else self.NIL_NODE

    def search(self, key: int) -> "Node":
        """
        Search for a node with key set to `key` in the BST rooted at `self`.
        :param key: Value for which the matching node's `key` attribute must match.

        Returns the first encountered matching node, or `None` if none exists.
        """
        if self.key == key:
            return self

        if key < self.key and self.left is not self.NIL_NODE:
            return self.left.search(key)

        if self.right is not self.NIL_NODE:
            return self.right.search(key)

        return None

    def transplant(self, new_node: "Node") -> None:
        """
        """
        if self == self.parent.left:
            self.parent.left = new_node
        else:
            self.parent.right = new_node

        if new_node is not self.NIL_NODE:
            new_node.parent = self.parent

        self.parent = self.NIL_NODE
