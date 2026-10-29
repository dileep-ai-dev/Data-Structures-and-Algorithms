
from collections import deque


class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        stack = [root]
        result = deque()

        while stack:
            node = stack.pop()
            result.appendleft(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return list(result)
