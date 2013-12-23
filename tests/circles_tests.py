#!/usr/bin/env python

from nose.tools import *
from circles import collision

def is_tree_equal(left, right):
    if left is None and right is not None:
        return False
    elif left is not None and right is None:
        return False
    elif left is None and right is None:
        return True
    if left == right:
        return is_tree_equal(left.left, right.left) and is_tree_equal(left.right, right.right)
    else:
        return False
    
def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_building_to_right():
    vals = ((1, 1), (2, 2))
    tree = collision.KDTree(vals, 2)

    root = collision.KDTree.Node((1,1), 0)
    root.right = collision.KDTree.Node((2, 2), 1)

    assert is_tree_equal(tree._root, root) == True, "Trees are NOT equal."

def test_building_to_left():
    vals = ((1, 1), (0, 2))
    tree = collision.KDTree(vals, 2)

    root = collision.KDTree.Node((1,1), 0)
    root.left = collision.KDTree.Node((0, 2), 1)

    assert is_tree_equal(tree._root, root) == True, "Trees are NOT equal."

def test_building_both_ways():
    vals = ((1, 1), (0, 0), (2, 2))
    tree = collision.KDTree(vals, 2)

    root = collision.KDTree.Node((1,1), 0)
    root.left = collision.KDTree.Node((0, 0), 1)
    root.right = collision.KDTree.Node((2, 2), 0)

    assert is_tree_equal(tree._root, root) == True, "Trees are NOT equal."

def test_three_nodes_depth_two():
    vals = ((1, 1), (0, 0), (0, 2))
    tree = collision.KDTree(vals, 2)

    root = collision.KDTree.Node((1,1), 0)
    root.left = collision.KDTree.Node((0, 0), 1)
    root.left.right = collision.KDTree.Node((0, 2), 1)

    assert is_tree_equal(tree._root, root) == True, "Trees are NOT equal."
