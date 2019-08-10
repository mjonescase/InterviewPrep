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


def search(node: Node, key: int) -> Node:
    """
    :param node: Node at the root of the tree to be searched.
    :param key: Value for which the matching node's `key` attribute must match.
    
    Returns the first encountered matching node, or `None` if none exists.
    """
    if node is None or node.key == key:
        return node

    if key < node.key:
        return search(node.left, key)

    return search(node.right, key)


def maximum(node: Node) -> Node:
    """
    :param node: Node at the root of the tree to be searched.

    Returns the Node in the tree containing the maximum key.
    """
    while node.right is not None:
        node = node.right

    return node


def minimum(node: Node) -> Node:
    """
    :param node: Node at the root of the tree to be searched.

    Returns the Node in the tree containing the minimum key.
    """
    while node.left is not None:
        node = node.left

    return node
