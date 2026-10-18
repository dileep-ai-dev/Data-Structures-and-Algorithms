
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    if root is None:
        return []

    queue = deque([root])
    result = []

    while queue:
        level_len = len(queue)
        current = []

        for _ in range(level_len):
            curr = queue.popleft()
            current.append(curr.val)

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        result.append(current)

    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(levelOrder(root))
