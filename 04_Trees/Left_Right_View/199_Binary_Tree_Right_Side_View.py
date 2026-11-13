
from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        right = []
        queue = deque([root])

        while queue:
            length = len(queue)
            right.append(queue[-1].val)

            for _ in range(length):
                num = queue.popleft()

                if num.left:
                    queue.append(num.left)

                if num.right:
                    queue.append(num.right)

        return right
