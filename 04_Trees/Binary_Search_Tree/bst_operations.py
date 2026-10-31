
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def BST(root, target):
    node = root

    while node:
        if node.data == target:
            return node.data
        elif target < node.data:
            node = node.left
        else:
            node = node.right

    return None


def insert_(root, value):
    if root is None:
        return TreeNode(value)

    node = root
    parent = None

    while node:
        parent = node

        if value < node.data:
            node = node.left
        elif value > node.data:
            node = node.right
        else:
            return root

    new_node = TreeNode(value)

    if value < parent.data:
        parent.left = new_node
    else:
        parent.right = new_node

    return root


def min_value(root):
    if root is None:
        return None

    node = root

    while node.left:
        node = node.left

    return node.data


def max_value(root):
    if root is None:
        return None

    node = root

    while node.right:
        node = node.right

    return node.data
