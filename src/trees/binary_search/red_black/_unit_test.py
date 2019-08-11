from hamcrest import assert_that, equal_to

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
