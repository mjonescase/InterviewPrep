"""
Stateless, functional binary tree algorithms
"""
from .Node import Node


def find_parent(root: Node, node: Node) -> Node:
    """
    :param root: The node at the root of the tree
    :param node: The node to insert
    """
    parent = None
    insert_point = root
    while insert_point:
        parent = insert_point
        if node.key < insert_point.key:
            # Per the convention in CLRS chapter 12.3,
            # right wins in a tie (keys are equal)
            insert_point = insert_point.left
        else:
            insert_point = insert_point.right

    return parent
