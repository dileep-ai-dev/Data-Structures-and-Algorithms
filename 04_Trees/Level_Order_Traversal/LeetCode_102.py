
from collections import deque

class Solution:
    def levelOrder(self, root):
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
