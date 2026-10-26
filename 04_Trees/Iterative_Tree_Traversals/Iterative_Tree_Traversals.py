
from collections import deque


class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def preorder_iterative(root):
    if root is None:
        return []

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.data)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


def inorder_iterative(root):
    stack = []
    result = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.data)
        current = current.right

    return result


def postorder_iterative(root):
    if root is None:
        return []

    stack = [root]
    result = deque()

    while stack:
        node = stack.pop()
        result.appendleft(node.data)

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return list(result)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print("Preorder:", preorder_iterative(root))
    print("Inorder:", inorder_iterative(root))
    print("Postorder:", postorder_iterative(root))
