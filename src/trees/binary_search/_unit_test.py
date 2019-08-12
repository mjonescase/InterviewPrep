from hamcrest import assert_that, equal_to, none

from . import BinarySearchTree
from .Node import Node


# INSERT
def test_insert_left_happy():
    tree = BinarySearchTree.BinarySearchTree()
    tree.insert(5)
    tree.insert(3)
    assert_that(tree.root.left.key, equal_to(3))
    assert_that(tree.root.right, none())


def test_insert_right_happy():
    tree = BinarySearchTree.BinarySearchTree()
    tree.insert(5)
    tree.insert(7)
    assert_that(tree.root.left, none())
    assert_that(tree.root.right.key, equal_to(7))


def test_insert_least_to_greatest():
    tree = BinarySearchTree.BinarySearchTree()
    tree.insert(5)
    tree.insert(7)
    tree.insert(9)
    assert_that(tree.root.left, none())
    assert_that(tree.root.right.key, equal_to(7))
    assert_that(tree.root.right.right.key, equal_to(9))


# SEARCH
def test_search_empty_tree():
    tree = BinarySearchTree.BinarySearchTree()
    assert_that(tree.search(5), none())


def test_search_root_happy():
    tree = BinarySearchTree.BinarySearchTree()
    tree.insert(5)
    assert_that(tree.search(5), equal_to(tree.root))


def test_search_root_left_child():
    tree = BinarySearchTree.BinarySearchTree()
    tree.insert(5)
    tree.insert(3)
    assert_that(tree.search(3), equal_to(tree.root.left))


def test_search_root_right_child():
    tree = BinarySearchTree.BinarySearchTree()
    tree.insert(5)
    tree.insert(7)
    assert_that(tree.search(7), equal_to(tree.root.right))


# MIN AND MAX
def test_max_empty():
    tree = BinarySearchTree.BinarySearchTree()
    assert_that(tree.maximum, none())


def test_max_happy():
    tree = BinarySearchTree.BinarySearchTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    assert_that(tree.maximum.key, equal_to(7))


def test_min_empty():
    tree = BinarySearchTree.BinarySearchTree()
    assert_that(tree.minimum, none())


def test_min_happy():
    tree = BinarySearchTree.BinarySearchTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    assert_that(tree.minimum.key, equal_to(3))


# SUCCESSOR
def test_successor_right_child():
    tree = BinarySearchTree.BinarySearchTree()
    under_test = tree.insert(5)
    _ = tree.insert(7)
    successor = tree.insert(6)
    _ = tree.insert(8)
    assert_that(under_test.successor, equal_to(successor))


def test_successor_non_root_no_right_child():
    tree = BinarySearchTree.BinarySearchTree()
    _ = tree.insert(10)
    _ = tree.insert(6)
    successor = tree.insert(14)
    under_test = tree.insert(12)
    _ = tree.insert(18)
    assert_that(under_test.successor, equal_to(successor))


def test_successor_largest_node():
    tree = BinarySearchTree.BinarySearchTree()
    _ = tree.insert(10)
    _ = tree.insert(6)
    _ = tree.insert(14)
    _ = tree.insert(12)
    under_test = tree.insert(18)
    assert_that(under_test.successor, none())


# PREDECESSOR
def test_predecessor_left_child():
    tree = BinarySearchTree.BinarySearchTree()
    under_test = tree.insert(5)
    predecessor = tree.insert(4)
    _ = tree.insert(3)
    assert_that(under_test.predecessor, equal_to(predecessor))


def test_predecessor_no_left_child():
    tree = BinarySearchTree.BinarySearchTree()
    _ = tree.insert(8)
    _ = tree.insert(5)
    _ = tree.insert(11)
    _ = tree.insert(9)
    predecessor = tree.insert(15)
    _ = tree.insert(14)
    _ = tree.insert(13)
    under_test = tree.insert(17)
    assert_that(under_test.predecessor, equal_to(predecessor))


def test_predecessor_smallest_node():
    tree = BinarySearchTree.BinarySearchTree()
    _ = tree.insert(8)
    under_test = tree.insert(5)
    _ = tree.insert(11)
    _ = tree.insert(9)
    _ = tree.insert(15)
    _ = tree.insert(14)
    _ = tree.insert(13)
    _ = tree.insert(17)
    assert_that(under_test.predecessor, none())


# TRANSPLANT
def test_transplant_root():
    tree = BinarySearchTree.BinarySearchTree()
    tree.insert(5)
    new_node = Node(6)
    tree.transplant(tree.root, new_node)
    assert_that(tree.root, equal_to(new_node))


def test_transplant_other():
    tree = BinarySearchTree.BinarySearchTree()
    _ = tree.insert(5)
    transplant_me = tree.insert(7)
    _ = tree.insert(3)
    new_node = Node(6)
    tree.transplant(transplant_me, new_node)
    assert_that(tree.root.right, equal_to(new_node))
    assert_that(new_node.parent, equal_to(tree.root))


def test_transplant_none():
    tree = BinarySearchTree.BinarySearchTree()
    _ = tree.insert(5)
    transplant_me = tree.insert(7)
    _ = tree.insert(3)
    tree.transplant(transplant_me, None)
    assert_that(tree.root.right, equal_to(None))


def test_delete_no_children():
    tree = BinarySearchTree.BinarySearchTree()
    _ = tree.insert(5)
    delete_me = tree.insert(3)
    tree.delete(delete_me)
    assert_that(tree.root.left, none())
    assert_that(delete_me.parent, none())


def test_delete_left_child_only():
    tree = BinarySearchTree.BinarySearchTree()
    _ = tree.insert(5)
    delete_me = tree.insert(8)
    _ = tree.insert(4)
    replacement = tree.insert(7)
    tree.delete(delete_me)
    assert_that(tree.root.right, equal_to(replacement))
    assert_that(replacement.parent, equal_to(tree.root))
    assert_that(delete_me.parent, none())


def test_delete_both_children_successor_direct():
    tree = BinarySearchTree.BinarySearchTree()
    _ = tree.insert(8)
    _ = tree.insert(6)
    delete_me = tree.insert(18)
    old_left = tree.insert(9)
    replacement = tree.insert(22)
    replacement_right = tree.insert(24)
    tree.delete(delete_me)
    assert_that(tree.root.right, equal_to(replacement))
    assert_that(replacement.parent, equal_to(tree.root))
    assert_that(replacement.left, equal_to(old_left))
    assert_that(old_left.parent, equal_to(replacement))
    assert_that(replacement.right, equal_to(replacement_right))
    assert_that(replacement_right.parent, equal_to(replacement))


def test_delete_both_children_successor_indirect():
    tree = BinarySearchTree.BinarySearchTree()
    _ = tree.insert(8)
    _ = tree.insert(6)
    delete_me = tree.insert(18)
    old_left = tree.insert(9)
    old_right = tree.insert(25)
    replacement = tree.insert(21)
    replacement_right = tree.insert(23)
    tree.delete(delete_me)
    assert_that(tree.root.right, equal_to(replacement))
    assert_that(replacement.parent, equal_to(tree.root))
    assert_that(replacement.left, equal_to(old_left))
    assert_that(old_left.parent, equal_to(replacement))
    assert_that(replacement.right, equal_to(old_right))
    assert_that(old_right.parent, equal_to(replacement))
    assert_that(old_right.left, equal_to(replacement_right))
    assert_that(replacement_right.parent, equal_to(old_right))
