from hamcrest import assert_that, equal_to, none

from . import BinarySearchTree


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


def xtest_search_root_left_child():
    tree = BinarySearchTree.BinarySearchTree()
    tree.insert(5)
    tree.insert(3)
    assert_that(tree.search(3), equal_to(tree.root.left))
