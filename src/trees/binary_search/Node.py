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
