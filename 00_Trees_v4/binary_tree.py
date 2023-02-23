import numpy as np
import typing

from node import Node
from binary_tree_visualization import visualize_tree
############################################################
# You can call visualize_tree(root: Node) to print a tree
############################################################

def count_leafs(root: Node) -> int:
    """
    Counts the number of leafs in a binary tree. Recursive function.

    :param root: The root of the (sub)tree
    :return: the number of leafs
    """
    
    # TODO: Implement this function

    raise NotImplementedError()


def get_height(root: Node) -> int:
    """
    Determines the height of a binary tree. Recursive function.

    :param root: The root of the (sub)tree
    :return: the height of the (sub)tree
    """
    
    # TODO: Implement this function

    raise NotImplementedError()


def get_highest_value(root: Node) -> int:
    """
    Gets the highest value out of a binary tree (not a binary search tree!!)
    Recursive function.

    :param root: The root of the (sub)tree
    :return: the highest value within this (sub)tree
    """

    # TODO: Implement this function

    raise NotImplementedError()


def get_greatest_smaller_value(root: Node) -> Node:
    """
    Returns the node with the greatest value smaller than the root.
    You can assume that this is a binary search tree. Also, you can
    assume that this function will only be used if such smaller values
    exists. Hint: This function is not recursive. Think of the binary 
    search tree property

    :param root: The root of the (sub)tree
    :return: the Node with the greatest value smaller than the root
    """

    # TODO: Implement this function

    raise NotImplementedError()


def get_smallest_greater_value(root: Node) -> Node:
    """
    Returns the node with the smallest value greater than the root.
    You can assume that this is a binary search tree. Also, you can
    assume that this function will only be used if such greater values
    exists. Hint: This function is not recursive. Think of the binary 
    search tree property

    :param root: The root of the (sub)tree
    :return: the Node with the smallest value greater than the root
    """

    # TODO: Implement this function

    raise NotImplementedError()


def is_binary_search_tree(root: Node) -> bool:
    """
    Returns whether the tree is a valid binary search tree. Hint:
    Recursive function. You can under some assumptions make use of
    get_smallest_greater_value and get_greatest_smaller_value.

    :param root: The root of the (sub)tree
    :return: true iff it is a valid binary search tree
    """

    # TODO: Implement this function

    raise NotImplementedError()


def search(root: Node, value: int) -> typing.Tuple[typing.Optional[Node], typing.Optional[Node]]:
    """
    Returns a Tuple with the following two items:
     - the parent of the node with a certain value
     - the node with a certain value
    Note that having access to the parent will prove useful
    other functions, such as adding and removing.

    If the binary search tree does not contain the value, return
    the parent of the node where it should have been
    placed, and a None value.

    :param root: The root of the (sub)tree
    :return: tuple of the nodes as described above
    """

    # TODO: Implement this function

    raise NotImplementedError()

def add(root: Node, value: int) -> bool:
    """
    Adds a new node to the binary search tree, respecting the condition that
    for each node all values in the left sub-tree are smaller than its value,
    and all values in the right subtree are greater than its value.
    Only adds the node with the value, if it does not exist yet in the tree.

    :param root: the root of the (sub)tree
    :param value: the value to be added
    :return: true upon success, false upon failure
    """

    # TODO: Implement this function

    raise NotImplementedError()


def remove(root: Node, value: int) -> typing.Tuple[bool, typing.Optional[Node]]:
    """
    Removes a node from the binary search tree, respecting the condition that
    for each node all values in the left sub-tree are smaller than its value,
    and all values in the right subtree are greater than its value.
    Only removes the node with the value, if it does exist in the tree.

    :param root: the root of the (sub)tree
    :param value: the value to be deleted
    :return: a Tuple consisting of
      - a boolean of whether the value was found and has been deleted
      - the root node of the new tree
    """

    # TODO: Implement this function

    raise NotImplementedError()

