
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:

        if not root:
            return []

        queue = deque([root])
        result = []
        left_to_right = True

        while queue:
            len_ = len(queue)
            curr_level = []

            for _ in range(len_):
                num = queue.popleft()
                curr_level.append(num.val)

                if num.left:
                    queue.append(num.left)

                if num.right:
                    queue.append(num.right)

            if not left_to_right:
                curr_level.reverse()

            left_to_right = not left_to_right
            result.append(curr_level)

        return result
