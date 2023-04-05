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
    number_leafs=0
    if root.left == None and root.right == None:
        return 1
    if root.left is not None:
        number_leafs += count_leafs(root.left)
    if root.right is not None:
        number_leafs += count_leafs(root.right)
    return number_leafs

    raise NotImplementedError()


def get_height(root: Node) -> int:
    """
    Determines the height of a binary tree. Recursive function.

    :param root: The root of the (sub)tree
    :return: the height of the (sub)tree
    """
    
    height = 0
    height_left=0
    height_right=0
    if root.left is not None:
        height_left +=1
        height_left += get_height(root.left)
    if root.right is not None: 
        height_right +=1
        height_right += get_height(root.right)
    height = max(height_left, height_right)
    return height

    raise NotImplementedError()


def get_highest_value(root: Node) -> int:
    """
    Gets the highest value out of a binary tree (not a binary search tree!!)
    Recursive function.

    :param root: The root of the (sub)tree
    :return: the highest value within this (sub)tree
    """

    highest_value_left = 0
    highest_value_right = 0
    if root.left is not None:
        highest_value_left = get_highest_value(root.left)
    if root.right is not None:
        highest_value_right = get_highest_value(root.right)
    highest_value=max(highest_value_left,highest_value_right,root.info)
    return highest_value

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

    if root.left is None:
        return root
    greatest_smaller_value=root.left
    while greatest_smaller_value.right is not None:
        greatest_smaller_value = greatest_smaller_value.right

    return greatest_smaller_value

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

    if root.right is None:
        return root
    smallest_greater_value=root.right
    while smallest_greater_value.left is not None:
        smallest_greater_value = smallest_greater_value.left

    return smallest_greater_value

    raise NotImplementedError()


def is_binary_search_tree(root: Node) -> bool:
    """
    Returns whether the tree is a valid binary search tree. Hint:
    Recursive function. You can under some assumptions make use of
    get_smallest_greater_value and get_greatest_smaller_value.

    :param root: The root of the (sub)tree
    :return: true iff it is a valid binary search tree
    """
    binary_search_tree=True

    if root.left is not None:
        binary_search_tree=is_binary_search_tree(root.left)
        if binary_search_tree is False:
            return False 
    if root.right is not None:
        binary_search_tree=is_binary_search_tree(root.right)    
        if binary_search_tree is False:
            return False

    if (root.left is None or root.left.info < root.info) and (root.right is None or root.right.info > root.info):
        return True
    return False


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

    
    if root.left is not None and root.left.info == value:
        return (root,root.left)
    if root.right is not None and root.right.info == value:
        return (root,root.right)
    if root.info == value:
        return (None, root)
    #Children not matching
    if root.left is not None and value < root.info:
        return search(root.left, value)
    elif root.right is not None and value > root.info:
        return search(root.right, value)
    #Case value does not exist
    return (root, None)
     

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
    parent, child = search(root, value)

    #Value already exists in tree -> finished
    if child is not None: return

    if value < parent.info:
        parent.left = Node(value, None, None)
        return True
    else: 
        parent.right = Node(value,None,None)
        return True
    return False


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
    parent, child = search(root, value)

    # #Value is root 
    # if parent is None: 
    #     left_subtree = root.left if root.left is not None else None
    #     right_subtree = root.right if root.right is not None else None
    #     return (True, Node(None,None,None))

    #Value does not exists in tree -> finished
    if child is None: return (False, root)

    #new child is picked from the subtree with the largest size
    height_left=0 if child.left is None else get_height(child.left)
    height_right=0 if child.right is None else get_height(child.right)

    #Deleting the child 
    #TODO: make it less complicated
    if height_left >= height_right:
        old_child = child
        child=child.left
        if old_child.right is not None:
            greatest_smaller_node=child
            while greatest_smaller_node.right is not None:
                greatest_smaller_node = greatest_smaller_node.right
            greatest_smaller_node.right = old_child.right
    else:
        old_child = child
        child=child.right
        if old_child.left is not None:
            smallest_greater_node=child
            while smallest_greater_node.left is not None:
                smallest_greater_node = smallest_greater_node.left
            smallest_greater_node.left = old_child.left

    #Assigning new child to tree
    if parent is None:
        root.info=child.info
        root.left=child.left
        root.right =child.right
        return (True, root)
    if parent.left is not None and parent.left.info == value:
        parent.left=child
        return (True, root)
    if parent.right is not None and parent.right.info == value:
        parent.right=child
        return (True, root)

    return (False, root)

    raise NotImplementedError()

