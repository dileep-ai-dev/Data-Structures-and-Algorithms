
from collections import deque


class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def top_view(root):
    if not root:
        return []

    queue = deque([(root, 0)])
    dict_ = {}

    while queue:
        num = queue.popleft()
        node = num[0]
        hd = num[1]

        if hd not in dict_:
            dict_[hd] = node.data

        if node.left:
            queue.append((node.left, hd - 1))

        if node.right:
            queue.append((node.right, hd + 1))

    return [dict_[key] for key in sorted(dict_)]


def bottom_view(root):
    if not root:
        return []

    queue = deque([(root, 0)])
    dict_ = {}

    while queue:
        num = queue.popleft()
        node = num[0]
        hd = num[1]

        dict_[hd] = node.data

        if node.left:
            queue.append((node.left, hd - 1))

        if node.right:
            queue.append((node.right, hd + 1))

    return [dict_[key] for key in sorted(dict_)]


# Example Binary Tree

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.right = TreeNode(4)

root.right.left = TreeNode(5)
root.right.right = TreeNode(6)

root.right.right.right = TreeNode(7)


print("Top View:", top_view(root))
print("Bottom View:", bottom_view(root))
