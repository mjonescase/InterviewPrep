from hamcrest import assert_that, equal_to

from .Color import Color
from .NilNode import NIL_NODE
from .RedBlackNode import RedBlackNode
from .RedBlackTree import RedBlackTree


# LEFT ROTATE
def test_left_rotate_both_children_populated():
    # set up
    tree = RedBlackTree()
    _ = tree.insert(5)
    left_rotate_me = tree.insert(7)
    _ = tree.insert(3)
    old_left = tree.insert(6)
    old_right = tree.insert(8)

    # act
    tree.left_rotate(left_rotate_me)

    # assert
    # old_right is now left_rotate_me's parent.
    assert_that(left_rotate_me.parent, equal_to(old_right))
    assert_that(old_right.left, equal_to(left_rotate_me))
    # left_rotate_me's left child is still old_left.
    assert_that(left_rotate_me.left, equal_to(old_left))
    assert_that(old_left.parent, equal_to(left_rotate_me))
    # old_right is now tree.root's right child.
    assert_that(tree.root.right, equal_to(old_right))
    assert_that(old_right.parent, equal_to(tree.root))


def test_left_rotate_tree_root():
    # set up
    tree = RedBlackTree()
    left_rotate_me = tree.insert(5)
    old_right = tree.insert(7)
    old_left = tree.insert(3)
    _ = tree.insert(6)
    _ = tree.insert(8)

    # act
    tree.left_rotate(left_rotate_me)

    # assert
    # old_right is now left_rotate_me's parent.
    assert_that(left_rotate_me.parent, equal_to(old_right))
    assert_that(old_right.left, equal_to(left_rotate_me))
    # left_rotate_me's left child is still old_left.
    assert_that(left_rotate_me.left, equal_to(old_left))
    assert_that(old_left.parent, equal_to(left_rotate_me))
    # old_right is now tree.root
    assert_that(tree.root, equal_to(old_right))
    assert_that(old_right.parent, equal_to(NIL_NODE))


# RIGHT ROTATE
def test_right_rotate_both_children_populated():
    # set up
    tree = RedBlackTree()
    _ = tree.insert(5)
    right_rotate_me = tree.insert(7)
    _ = tree.insert(3)
    old_left = tree.insert(6)
    old_right = tree.insert(8)

    # act
    tree.right_rotate(right_rotate_me)

    # assert
    # old_left is now right_rotate_me's parent.
    assert_that(right_rotate_me.parent, equal_to(old_left))
    assert_that(old_left.right, equal_to(right_rotate_me))
    # right_rotate_me's left child is still old_right.
    assert_that(right_rotate_me.right, equal_to(old_right))
    assert_that(old_right.parent, equal_to(right_rotate_me))
    # old_left is now tree.root's right child.
    assert_that(tree.root.right, equal_to(old_left))
    assert_that(old_left.parent, equal_to(tree.root))


def test_right_rotate_tree_root():
    # set up
    tree = RedBlackTree()
    right_rotate_me = tree.insert(5)
    old_right = tree.insert(7)
    old_left = tree.insert(3)
    _ = tree.insert(6)
    _ = tree.insert(8)

    # act
    tree.right_rotate(right_rotate_me)

    # assert
    # old_left is now right_rotate_me's parent.
    assert_that(right_rotate_me.parent, equal_to(old_left))
    assert_that(old_left.right, equal_to(right_rotate_me))
    # right_rotate_me's right child is still old_right.
    assert_that(right_rotate_me.right, equal_to(old_right))
    assert_that(old_right.parent, equal_to(right_rotate_me))
    # old_left is now tree.root
    assert_that(tree.root, equal_to(old_left))
    assert_that(old_left.parent, equal_to(NIL_NODE))


# UNCLE
def test_uncle_root():
    tree = RedBlackTree()
    _ = tree.insert(5)
    assert_that(tree.root.uncle, equal_to(NIL_NODE))


def test_uncle_left():
    tree = RedBlackTree()
    _ = tree.insert(5)
    uncle = tree.insert(3)
    _ = tree.insert(7)
    node = tree.insert(6)
    _ = tree.insert(8)
    assert_that(node.uncle, equal_to(uncle))


def test_uncle_right():
    tree = RedBlackTree()
    _ = tree.insert(5)
    _ = tree.insert(3)
    uncle = tree.insert(7)
    node = tree.insert(4)
    _ = tree.insert(2)
    assert_that(node.uncle, equal_to(uncle))


def test_insert_fixup_both_case_1():
    """
    Case in which the node's uncle is red.
    Whether the uncle is the right or left child of
    node's grandparent is irrelevant for case 1.
    """
    # setup
    tree = RedBlackTree()
    make_black_a = tree.insert(5)
    uncle = tree.insert(3)
    parent = tree.insert(7)
    node = tree.insert(6)
    make_black_a.color = Color.BLACK

    # run
    tree.insert_fixup(node)

    # assert
    assert_that(parent.color, equal_to(Color.BLACK))
    assert_that(uncle.color, equal_to(Color.BLACK))
    assert_that(node.color, equal_to(Color.RED))
    assert_that(tree.root.color, equal_to(Color.BLACK))
