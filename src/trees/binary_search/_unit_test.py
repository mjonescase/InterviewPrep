from hamcrest import assert_that, equal_to, none

from . import BinarySearchTree


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
