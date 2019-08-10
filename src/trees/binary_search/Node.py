class Node(object):
    """
    Represents a node in a binary search tree,
    where the keys are `int`s.
    """

    key: int
    parent: "Node"
    left: "Node"
    right: "Node"

    def __init__(
        self, key: int, parent: "Node" = None, left: "Node" = None, right: "Node" = None
    ):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    @property
    def maximum(self) -> "Node":
        """
        :param node: Node at the root of the tree to be searched.

        Returns the Node in the tree containing the maximum key.
        """
        if self.right is None:
            return self

        return self.right.maximum

    @property
    def minimum(self) -> "Node":
        """
        :param node: Node at the root of the tree to be searched.

        Returns the Node in the tree containing the minimum key.
        """
        if self.left is None:
            return self

        return self.left.minimum

    @property
    def successor(self) -> "Node":
        """
        Returns the node with the smallest key greater than `self.key`
        """
        if self.right is not None:
            return self.right.minimum

        current = self
        parent = self.parent
        while parent is not None and current == parent.right:
            current = parent
            parent = parent.parent

        return parent

    @property
    def predecessor(self) -> "Node":
        if self.left is not None:
            return self.left.maximum

        current = self
        parent = self.parent
        while parent is not None and current == parent.left:
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
        while insert_point:
            parent = insert_point
            if self.key < insert_point.key:
                # Per the convention in CLRS chapter 12.3,
                # right wins in a tie (keys are equal)
                insert_point = insert_point.left
            else:
                insert_point = insert_point.right

        return parent

    def search(self, key: int) -> "Node":
        """
        Search for a node with key set to `key` in the BST rooted at `self`.
        :param key: Value for which the matching node's `key` attribute must match.

        Returns the first encountered matching node, or `None` if none exists.
        """
        if self.key == key:
            return self

        if key < self.key and self.left is not None:
            return self.left.search(key)

        if self.right is not None:
            return self.right.search(key)

        return None
